#!/usr/bin/env python3
"""RL-Frontier 每日 arXiv 论文 agent（纯 arXiv 数据源）。

流程：
  1. arXiv API 拉取最新 RL 论文（submittedDate 降序，过滤已处理，单次 ≤ max_papers 篇）
  2. 每篇论文一个独立目录 papers/<日期>/<论文标题>/（目录名即论文标题）
  3. 下载 PDF 到本地 + pdftotext 转文本（供解读用；PDF/txt 留本地，不入库）
  4. 调用 opencode run 生成简明中文核心解读 README.md
  5. 重建当日 papers/<日期>/INDEX.md 速览表
  6. git commit & push（仓库 remote 已内嵌本账户 token，走代理）

用法：
  python3 scripts/daily_agent.py --run-now [--max-papers 50] [--no-push] [--no-pdf]
  python3 scripts/daily_agent.py --daemon          # 每天 UTC 01:00（北京 09:00）自动运行

状态/日志/锁在仓库外 ../agent_state/，与容器内其他账户环境完全隔离。
"""
import argparse
import fcntl
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

REPO = Path(__file__).resolve().parents[1]
STATE_DIR = REPO.parent / "agent_state"
STATE_FILE = STATE_DIR / "processed.json"
LOCK_FILE = STATE_DIR / "agent.lock"
PID_FILE = STATE_DIR / "daemon.pid"
PAPERS_DIR = REPO / "papers"

PROXY = "http://agent.baidu.com:8891"
UA = "Mozilla/5.0 (X11; Linux x86_64) RL-Frontier-Agent/1.0"
ARXIV_API = "https://export.arxiv.org/api/query"
ARXIV_QUERY = ('(abs:"reinforcement learning" OR abs:RLHF OR abs:RLVR) '
               'AND (cat:cs.LG OR cat:cs.AI OR cat:cs.CL)')
FETCH_RESULTS = 150
DEFAULT_LIMIT = 50
OPENCODE_BIN = "/root/.opencode/bin/opencode"
OPENCODE_TIMEOUT = 600
PDF_TEXT_CHARS = 15000
MAX_PDF_MB = 30
MAX_ATTEMPTS = 3
RUN_HOUR_UTC = 1

ATOM = "{http://www.w3.org/2005/Atom}"

PROMPT_TMPL = """你是 RL-Frontier 仓库（追踪强化学习前沿论文）的解读助手。
请为下面这篇 arXiv 论文写一份"核心解读"，写入这个文件：
{readme_abs}

【硬性要求】
1. 只允许写入上面这一个文件（它是 papers/ 下该论文专属目录里的 README.md）。严禁修改仓库根目录的 README.md 或其他任何文件；不要执行 git 命令；不要联网搜索。
2. 中文，简明扼要，正文 200~400 字。读者是工程师/研究员：抓核心、说人话，不要公式推导，不要堆砌术语。
3. 正文结构固定为四个小节：
## 一句话概括
## 核心方法
## 关键结果
## 为什么值得关注
4. 文件开头写 YAML frontmatter，按下面模板原样填写（title/arxiv/url/authors/published 用我给的值；tagline 用你自己的一句话概括，30 字以内、不以句号结尾）：
---
title: "{title}"
arxiv: "{arxiv_id}"
url: {url}
authors: "{authors}"
published: {published}
tagline: "{tagline}"
---
5. 完成后只输出 DONE。

【论文信息】
- 标题：{title}
- 作者：{authors}
- arXiv：{arxiv_id}（{url}）
- 发布时间：{published}

【摘要】
{abstract}

{fulltext_section}"""

FULLTEXT_TMPL = """【论文 PDF 全文文本（前 {n} 字符，帮助你理解方法细节；解读里只提炼核心，不要照抄）】
{text}"""


def log(msg):
    print("[%s] %s" % (datetime.now(timezone.utc).strftime("%m-%d %H:%M:%S"), msg), flush=True)


def bj_today():
    return (datetime.now(timezone.utc) + timedelta(hours=8)).strftime("%Y-%m-%d")


def http_get(url, timeout=60, binary=False, retries=2):
    last = None
    for _ in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read()
            return data if binary else data.decode("utf-8", "ignore")
        except Exception as e:
            last = e
            time.sleep(5)
    raise last


def load_state():
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"processed": {}, "last_run_date": None}


def save_state(state):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    tmp = STATE_FILE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(STATE_FILE)


def strip_control(s):
    return re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", "", s)


def fetch_entries():
    url = ARXIV_API + "?" + urllib.parse.urlencode({
        "search_query": ARXIV_QUERY,
        "sortBy": "submittedDate", "sortOrder": "descending",
        "max_results": FETCH_RESULTS})
    root = ET.fromstring(http_get(url, timeout=90))
    out = []
    for e in root.findall(ATOM + "entry"):
        raw_id = e.findtext(ATOM + "id", "") or ""
        m = re.search(r"abs/(.+)$", raw_id)
        if not m:
            continue
        arxiv_id = re.sub(r"v\d+$", "", m.group(1))
        title = re.sub(r"\s+", " ", e.findtext(ATOM + "title", "") or "").strip()
        abstract = re.sub(r"\s+", " ", e.findtext(ATOM + "summary", "") or "").strip()
        if not title or not abstract:
            continue
        authors = [a.findtext(ATOM + "name", "") for a in e.findall(ATOM + "author")]
        published = e.findtext(ATOM + "published", "") or ""
        out.append({
            "arxiv_id": arxiv_id,
            "title": title,
            "abstract": abstract,
            "authors": ", ".join(a for a in authors[:6] if a) + (", et al." if len(authors) > 6 else ""),
            "published": published[:10],
            "url": "https://arxiv.org/abs/" + arxiv_id,
        })
    return out


def slugify(title):
    s = re.sub(r"[^0-9A-Za-z\-\.,+ ]", "", title)
    s = re.sub(r"\s+", "-", s.strip())
    s = re.sub(r"-{2,}", "-", s).strip("-.")
    return (s[:100] or "untitled").rstrip(".-")


def fetch_pdf_text(pdir, paper):
    if not paper.get("want_pdf", True):
        return ""
    pdf_path = pdir / "paper.pdf"
    if not (pdf_path.exists() and pdf_path.stat().st_size > 10240):
        try:
            data = http_get("https://arxiv.org/pdf/" + paper["arxiv_id"],
                            timeout=180, binary=True, retries=1)
            if not data.startswith(b"%PDF") or len(data) > (MAX_PDF_MB << 20):
                return ""
            pdf_path.write_bytes(data)
        except Exception:
            return ""
    txt_path = pdir / "paper.txt"
    if txt_path.exists() and txt_path.stat().st_size > 2000:
        return txt_path.read_text(encoding="utf-8", errors="ignore")[:PDF_TEXT_CHARS]
    try:
        r = subprocess.run(["pdftotext", "-q", str(pdf_path), "-"],
                           capture_output=True, text=True, timeout=120)
        text = r.stdout or ""
    except Exception:
        return ""
    if len(text) < 2000:
        return ""
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    txt_path.write_text(text, encoding="utf-8")
    return text[:PDF_TEXT_CHARS]


def build_prompt(paper, fulltext, pdir):
    ft = ""
    if fulltext:
        ft = FULLTEXT_TMPL.format(n=len(fulltext), text=fulltext)
    else:
        ft = "（未能获取 PDF 全文，请仅基于摘要完成解读，并在'关键结果'末尾注明'（基于摘要）'。）"
    return PROMPT_TMPL.format(
        readme_abs=str((pdir / "README.md").resolve()),
        title=paper["title"], arxiv_id=paper["arxiv_id"], url=paper["url"],
        authors=paper["authors"], published=paper["published"],
        tagline="（由你填写：一句话概括，30字以内，不以句号结尾）",
        abstract=strip_control(paper["abstract"]), fulltext_section=strip_control(ft))


def run_opencode(pdir, prompt, mode=""):
    env = {k: v for k, v in os.environ.items()
           if k.lower() not in ("http_proxy", "https_proxy", "all_proxy", "ftp_proxy")}
    env["PATH"] = os.path.dirname(OPENCODE_BIN) + ":" + env.get("PATH", "")
    try:
        r = subprocess.run([OPENCODE_BIN, "run", prompt], cwd=str(pdir),
                           capture_output=True, text=True, timeout=OPENCODE_TIMEOUT, env=env)
    except subprocess.TimeoutExpired:
        log("opencode 超时%s" % mode)
        return False
    if r.returncode == 0 and (pdir / "README.md").exists():
        return True
    err = re.sub(r"\x1b\[[0-9;]*m", "", (r.stderr or "") + " | " + (r.stdout or ""))
    log("opencode 失败%s rc=%s: %s" % (mode, r.returncode,
        re.sub(r"\s+", " ", err).strip()[-280:]))
    return False


def parse_frontmatter(text):
    m = re.match(r"^\s*---\s*\n(.*?)\n---\s*\n?", text, re.S)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"(\w+):\s*(.*)", line.strip())
        if mm:
            fm[mm.group(1)] = mm.group(2).strip().strip('"')
    return fm, text[m.end():]


def esc(s):
    return s.replace('"', "'").strip()


def first_line_after_h2(body, h2):
    m = re.search(r"##\s*%s\s*\n+\s*(.+)" % re.escape(h2), body)
    if not m:
        return ""
    return m.group(1).strip().lstrip("-*• ").replace("**", "")[:80]


def normalize_readme(pdir, paper):
    path = pdir / "README.md"
    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    tagline = fm.get("tagline") or first_line_after_h2(body, "一句话概括") or paper["title"]
    body = body.lstrip("\n")
    if not body.startswith("#"):
        body = "# " + paper["title"] + "\n\n" + body
    fm_text = ("---\n"
               'title: "%s"\n'
               'arxiv: "%s"\n'
               'url: %s\n'
               'authors: "%s"\n'
               'published: %s\n'
               'tagline: "%s"\n'
               "---\n\n" % (esc(paper["title"]), paper["arxiv_id"], paper["url"],
                            esc(paper["authors"]), paper["published"], esc(tagline[:60])))
    path.write_text(fm_text + body, encoding="utf-8")


def guard_repo_readme():
    r = git("status", "--porcelain", "--", "README.md", check=False)
    if r.stdout.strip():
        git("checkout", "--", "README.md")
        log("警告：仓库主 README.md 被误写，已自动恢复")


def process_paper(paper, state):
    key = paper["arxiv_id"]
    rec = state["processed"].setdefault(key, {"attempts": 0, "status": "new"})
    if rec["status"] == "done" or rec["status"] == "skipped":
        return False
    if rec["attempts"] >= MAX_ATTEMPTS:
        rec["status"] = "skipped"
        save_state(state)
        log("SKIP（多次失败）: %s" % paper["title"][:60])
        return False
    rec["attempts"] += 1
    rec["title"] = paper["title"]

    pdir = PAPERS_DIR / paper["published"] / slugify(paper["title"])
    pdir.mkdir(parents=True, exist_ok=True)
    log("[%d/%d] %s -> %s" % (rec["attempts"], MAX_ATTEMPTS, paper["title"][:60], pdir.relative_to(REPO)))

    try:
        if not (pdir / "README.md").exists():
            fulltext = fetch_pdf_text(pdir, paper)
            if not run_opencode(pdir, build_prompt(paper, fulltext, pdir), mode="(全文)"):
                time.sleep(5)
                if not run_opencode(pdir, build_prompt(paper, "", pdir), mode="(仅摘要)"):
                    raise RuntimeError("opencode 全文/摘要两种模式均失败")
        normalize_readme(pdir, paper)
        r = git("status", "--porcelain", "--", "README.md", check=False)
        if r.stdout.strip():
            git("checkout", "--", "README.md")
            log("警告：仓库主 README 被误写，已自动恢复")
        rec.update({"status": "done", "date": paper["published"],
                    "dir": str(pdir.relative_to(REPO))})
        save_state(state)
        return paper["published"]
    except Exception as e:
        guard_repo_readme()
        log("FAIL: %s | %s" % (paper["title"][:60], e))
        rec["status"] = "failed"
        rec["error"] = str(e)[:300]
        save_state(state)
        return False


def rebuild_index(date_dir):
    rows = []
    for sub in sorted(date_dir.iterdir()):
        rm = sub / "README.md"
        if not sub.is_dir() or not rm.exists():
            continue
        fm, _ = parse_frontmatter(rm.read_text(encoding="utf-8"))
        rows.append((fm.get("title", sub.name), fm.get("tagline", ""), sub.name))
    if not rows:
        return False
    lines = ["# RL 前沿日报 · %s（%d 篇）" % (date_dir.name, len(rows)), "",
             "| # | 论文 | 一句话概括 |", "|---|------|-----------|"]
    for i, (t, tag, d) in enumerate(rows, 1):
        lines.append("| %d | [%s](%s/README.md) | %s |" % (
            i, t.replace("|", "/"), urllib.parse.quote(d), tag.replace("|", "/")))
    lines += ["", "*由 RL-Frontier daily agent 自动生成 · 数据源 arXiv API*"]
    (date_dir / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return True


WEEKLY_PROMPT = """你是 RL-Frontier 仓库（追踪强化学习前沿论文）的周报撰写助手。
请基于下面这份"本周 arXiv RL 论文清单"，写一份中文周报，写入这个文件：
{out_abs}

【硬性要求】
1. 只允许写入上面这一个文件；严禁修改仓库其他文件；不要执行 git 命令；不要联网。
2. 文件开头写 YAML frontmatter：
---
title: "RL 前沿周报 {start} ~ {end}"
range: {start}..{end}
papers: {n}
tagline: "（你的一句话本周趋势概括，30字以内）"
---
3. 正文结构：
# RL 前沿周报：{start} ~ {end}

## 本周总览
（2~4 句：数量、整体热度、最突出的方向）

## 主题聚类
（把论文聚成 4~6 个主题；每个主题用 `### 主题名` 小节：先用 2~3 句点评该主题本周的动向，再列代表论文（3~6 篇，格式：`- [标题](arXiv链接) —— 一句话`））

## 本周最值得深读的 5 篇
（编号列表：标题 + 链接 + 1~2 句入选理由；优先挑方法有新意、可能影响后续工作的）

## 趋势观察
（3~5 条 bullet：与近几周相比的变化、反复出现的 idea、值得跟踪的苗头；没有把握的不要编造）

4. 语言：中文、简明、有观点；不要空话套话；不得编造清单之外的论文。
5. 完成后只输出 DONE。

【本周论文清单（日期 | 标题 | arXiv）】
{listing}"""


def rebuild_root_index():
    lines = ["# RL-Frontier 论文总索引", "",
             "> 每日自动更新 · 数据源 arXiv API · 点击日期进入当日速览与解读目录", ""]
    total = 0
    days = 0
    for date_dir in sorted(PAPERS_DIR.iterdir(), reverse=True):
        if not date_dir.is_dir() or not re.match(r"^\d{4}-\d{2}-\d{2}$", date_dir.name):
            continue
        n = len([d for d in date_dir.iterdir()
                 if d.is_dir() and (d / "README.md").exists()])
        if n == 0:
            continue
        lines.append("- [%s](%s/INDEX.md)（%d 篇）" % (date_dir.name, date_dir.name, n))
        total += n
        days += 1
    lines += ["", "*共 %d 天 / %d 篇 · 由 daily agent 自动生成*" % (days, total)]
    (PAPERS_DIR / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def weekly_review():
    state = load_state()
    today = datetime.now(timezone.utc).date()
    start = (today - timedelta(days=6)).isoformat()
    items = sorted((v["date"], v["title"], "https://arxiv.org/abs/" + k)
                   for k, v in state["processed"].items()
                   if v.get("status") == "done" and start <= v.get("date", "") <= today.isoformat())
    if len(items) < 10:
        log("周报素材不足（%d 篇），跳过" % len(items))
        return False
    listing = "\n".join("%s | %s | %s" % (d, t, u) for d, t, u in items)
    notes_dir = REPO / "notes"
    notes_dir.mkdir(exist_ok=True)
    out_name = "weekly-%s_%s.md" % (start, today.isoformat())
    out_abs = (notes_dir / out_name).resolve()
    prompt = WEEKLY_PROMPT.format(out_abs=out_abs, start=start,
                                  end=today.isoformat(), n=len(items), listing=listing)
    run_opencode(notes_dir, prompt, mode="(周报)")
    if not (notes_dir / out_name).exists():
        return False
    fm_text = (notes_dir / out_name).read_text(encoding="utf-8")
    if not fm_text.lstrip().startswith("---"):
        (notes_dir / out_name).write_text(
            "---\ntitle: \"RL 前沿周报 %s ~ %s\"\nrange: %s..%s\npapers: %d\n---\n\n"
            % (start, today.isoformat(), start, today.isoformat(), len(items)) + fm_text,
            encoding="utf-8")
    log("周报已生成: notes/%s" % out_name)
    return True


def git(*args, check=True):
    env = dict(os.environ)
    env["GIT_TERMINAL_PROMPT"] = "0"
    r = subprocess.run(["git", "-C", str(REPO)] + list(args),
                       capture_output=True, text=True, env=env)
    if check and r.returncode != 0:
        raise RuntimeError("git %s 失败: %s" % (" ".join(args), r.stderr.strip()))
    return r


def commit_push(msg):
    r = git("status", "--porcelain", "--", "papers", "notes", check=False)
    if not r.stdout.strip():
        log("无待提交变更")
        return
    git("add", "papers", "notes")
    git("commit", "-m", msg)
    for i in range(3):
        r = git("push", "origin", "main", check=False)
        if r.returncode == 0:
            log("已推送: %s" % msg)
            return
        log("push 失败（第 %d 次），重试: %s" % (i + 1, r.stderr.strip()[:200]))
        time.sleep(15)
    log("push 最终失败，变更已保留在本地 commit")


def run_once(args):
    state = load_state()
    entries = fetch_entries()
    log("arXiv 最新条目 %d 个" % len(entries))
    todo = [e for e in entries
            if state["processed"].get(e["arxiv_id"], {}).get("status") != "done"
            and state["processed"].get(e["arxiv_id"], {}).get("status") != "skipped"]
    todo = todo[: args.max_papers]
    if not todo:
        log("无新增论文")
        state["last_run_date"] = bj_today()
        save_state(state)
        return
    log("本次处理 %d 篇" % len(todo))
    touched = set()
    n_done = 0
    for paper in todo:
        d = process_paper(paper, state)
        if d:
            touched.add(d)
            n_done += 1
    for d in sorted(touched):
        rebuild_index(PAPERS_DIR / d)
    rebuild_root_index()
    if not args.no_push:
        commit_push("digest(%s): +%d papers (arXiv)" % (bj_today(), n_done))
    state["last_run_date"] = bj_today()
    save_state(state)
    log("完成：成功 %d / %d" % (n_done, len(todo)))


def next_run_utc():
    now = datetime.now(timezone.utc)
    target = now.replace(hour=RUN_HOUR_UTC, minute=0, second=0, microsecond=0)
    if target <= now:
        target += timedelta(days=1)
    return target


def _locked_run_once(args):
    lock = open(LOCK_FILE, "w")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        log("另一个实例在运行，本次跳过")
        return
    try:
        run_once(args)
    except Exception:
        import traceback
        traceback.print_exc()
    finally:
        try:
            fcntl.flock(lock, fcntl.LOCK_UN)
        except OSError:
            pass
        lock.close()


def run_daemon(args):
    PID_FILE.write_text(str(os.getpid()))
    log("daemon 启动 pid=%s，每天 UTC %02d:00（北京 %02d:00）运行"
        % (os.getpid(), RUN_HOUR_UTC, RUN_HOUR_UTC + 8))
    state = load_state()
    if state.get("last_run_date") != bj_today():
        _locked_run_once(args)
    while True:
        target = next_run_utc()
        wait = (target - datetime.now(timezone.utc)).total_seconds()
        log("下次运行: %s UTC（%.1f 小时后）" % (target.strftime("%Y-%m-%d %H:%M"), wait / 3600))
        time.sleep(min(wait, 3600))
        if datetime.now(timezone.utc) >= target:
            _locked_run_once(args)
            if datetime.now(timezone.utc).weekday() == 0:
                try:
                    if weekly_review():
                        commit_push("notes: weekly review (%s)" % bj_today())
                except Exception:
                    import traceback
                    traceback.print_exc()


def main():
    p = argparse.ArgumentParser(description="RL-Frontier 每日 arXiv 论文 agent")
    p.add_argument("--run-now", action="store_true", help="立即运行一次")
    p.add_argument("--daemon", action="store_true", help="守护进程模式（每天定时，周一附周报）")
    p.add_argument("--weekly", action="store_true", help="立即生成本周周报（notes/weekly-*.md）")
    p.add_argument("--max-papers", type=int, default=DEFAULT_LIMIT, help="单次最多处理篇数（默认 50）")
    p.add_argument("--no-push", action="store_true", help="只生成不推送")
    p.add_argument("--no-pdf", action="store_true", help="不下载 PDF，仅用摘要生成解读")
    args = p.parse_args()

    for k in ("http_proxy", "https_proxy", "HTTP_PROXY", "HTTPS_PROXY"):
        os.environ[k] = PROXY

    if args.daemon:
        run_daemon(args)
    elif args.weekly:
        if weekly_review():
            commit_push("notes: weekly review (%s)" % bj_today())
    elif args.run_now:
        _locked_run_once(args)
    else:
        p.print_help()


if __name__ == "__main__":
    main()
