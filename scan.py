#!/usr/bin/env python3
"""Scan GitHub for new DSH plugins since last push, verify root manifest, classify."""
import re, os, json, time, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.abspath(__file__))
verify = json.load(open(os.path.join(ROOT, "_verify.json"), encoding="utf-8"))
existing = set(verify["existing_repos"])
existing_lower = {r.lower() for r in existing}

# Section header exact strings (must match README exactly for insertion anchoring)
SECTIONS = {
    "外观": "### 🎨 外观 / 主题 / 字体",
    "余额": "### 💰 余额 / 用量 / 计费（涨→红、跌→绿，遵循 A 股习惯）",
    "文件": "### 📎 文件上传 / 拖拽 / `@file` 引用",
    "工作台": "### 🗂️ 文件树 / 编辑器 / 工作台（类 IDE）",
    "终端": "### 🖥️ 终端",
    "桌面壳": "### 🪟 桌面壳 / 启动器 / 系统托盘",
    "移动端": "### 📱 移动端 / 响应式",
    "记忆": "### 🧠 记忆 / AGI / 上下文",
    "会话": "### 💬 会话管理 / 导入导出",
    "提示词": "### ✨ 提示词优化 / 润色",
    "导航": "### 🧭 导航 / 大纲 / 跳转（长会话必备）",
    "TUI": "### ⌨️ 终端 TUI / 全屏界面",
    "桌宠": "### 🐳 桌面宠物",
    "语音": "### 🎙️ 语音 / 音频通话",
    "行情": "### 📈 行情 / 股票（A 股红涨绿跌）",
    "浏览器": "### 🌐 浏览器 / 网页交互",
    "MCP": "### 🔀 MCP / 设置扩展",
    "安全": "### 🔒 安全与权限",
    "智能体": "### 🤖 智能体 / 研究 / 创作",
    "文档": "### 📄 文档与渲染",
    "技能": "### 🧩 技能 / 提示词库 / 任务看板",
    "工作流": "### 🔁 工作流 / 自动化",
    "身份通信": "### 🔌 身份与通信 / 桥接",
    "开发运行时": "### 🧑‍💻 开发 / 运行时 / Profile",
}

# Keyword -> section, ordered by priority (first match wins)
RULES = [
    ("余额", ["balance", "billing", "usage", "cost", "quota", "token-analytics", "计费", "用量", "余额", "订阅", "subscription"]),
    ("行情", ["stock", "行情", "股价", "trading", "crypto", "基金", "a股", "market-data"]),
    ("桌宠", ["pet", "桌宠", "whale-girl", "宠物", "live2d", "desktop-pet"]),
    ("语音", ["voice", "tts", "asr", "语音", "audio", "stt", "speech", "sound"]),
    ("移动端", ["mobile", "ios", "android", "移动", "remote", "lan-link", "tauri"]),
    ("桌面壳", ["desktop", "tray", "launcher", "shell", "gui-shell", "启动器", "系统托盘", "deeptail"]),
    ("TUI", ["tui", "terminal-ui", "curses", "fullscreen"]),
    ("终端", ["terminal", "shell", "cli", "bash", "zsh", "终端", "command-line"]),
    ("浏览器", ["browser", "web", "playwright", "selenium", "crawl", "网页", "search-web", "fetch"]),
    ("MCP", ["mcp", "model-context", "设置扩展"]),
    ("安全", ["security", "permission", "auth", "guard", "审计", "权限", "安全", "defend", "approval", "sandbox"]),
    ("记忆", ["memory", "remember", "recall", "context", "记忆", "knowledge", "obsidian", "笔记"]),
    ("会话", ["session", "chat", "conversation", "import", "archive", "会话", "对话", "retrace", "history"]),
    ("导航", ["nav", "outline", "jump", "大纲", "导航", "toc", "bookmark"]),
    ("提示词", ["prompt", "提示词", "polish", "润色", "instruction"]),
    ("文档", ["doc", "markdown", "render", "pdf", "ppt", "文档", "report", "diagram", "mindmap", "note"]),
    ("技能", ["skill", "技能", "taskboard", "任务看板", "task-board", "prompt-lib"]),
    ("工作流", ["workflow", "automation", "cron", "schedule", "agent-team", "swarm", "工作流", "自动化", "定时", "plan"]),
    ("身份通信", ["wechat", "qq", "im", "discord", "telegram", "slack", "bridge", "微信", "企微", "通信", "chatops", "dingtalk", "lark", "feishu"]),
    ("智能体", ["agent", "research", "智能体", "subagent", "multi-agent", "deep-research", "crew"]),
    ("文件", ["file", "upload", "drag", "附件", "文件", "@file", "attachment"]),
    ("工作台", ["workbench", "editor", "ide", "file-tree", "文件树", "编辑器", "workspace", "侧边", "sidebar", "sidebar"]),
    ("开发运行时", ["dev", "runtime", "profile", "codex", "opencode", "plugin-dev", "开发", "运行时", "lsp", "debug", "git", "review"]),
    ("外观", ["theme", "ui", "skin", "wallpaper", "font", "外观", "主题", "皮肤", "壁纸", "style", "layout", "视觉", "animation"]),
]

def classify(name, desc):
    blob = (name + " " + desc).lower()
    for sec, kws in RULES:
        for kw in kws:
            if kw.lower() in blob:
                return sec
    return "开发运行时"  # fallback

def github_search(topic, since, page, per_page=30):
    q = f"topic:{topic}+pushed:>{since}"
    url = f"https://api.github.com/search/repositories?q={urllib.parse.quote(q, safe=':>+')}&sort=updated&order=desc&per_page={per_page}&page={page}"
    req = urllib.request.Request(url, headers={"User-Agent": "dsh-sync", "Accept": "application/vnd.github+json"})
    last_err = None
    for attempt in range(10):
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            # 5xx are transient (504 gateway timeouts); retry with backoff.
            if e.code in (500, 502, 503, 504):
                last_err = e
                time.sleep(8 + attempt * 4)
                continue
            raise  # 403/422/400 -> let caller decide (hard limits / rate limit)
        except Exception as e:
            last_err = e
            time.sleep(5)
            continue
    raise last_err

def fetch_raw(owner, name, branch):
    # primary: raw.githubusercontent.com
    url = f"https://raw.githubusercontent.com/{owner}/{name}/{branch}/package.json"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "dsh-sync"})
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.read().decode("utf-8", "replace")
    except Exception:
        pass
    # fallback: api.github.com contents endpoint (base64) — resilient to raw outages
    api = f"https://api.github.com/repos/{owner}/{name}/contents/package.json?ref={branch}"
    try:
        req = urllib.request.Request(api, headers={"User-Agent": "dsh-sync", "Accept": "application/vnd.github+json"})
        with urllib.request.urlopen(req, timeout=20) as r:
            import base64
            data = json.loads(r.read().decode("utf-8", "replace"))
            return base64.b64decode(data.get("content", "")).decode("utf-8", "replace")
    except Exception:
        return None

def has_dsh_bundle(pkg):
    if not pkg:
        return False
    if '"dsh"' in pkg and '"bundle"' in pkg:
        return True
    if "cordis.patch.yml" in pkg:
        return True
    return False

# We don't import urllib.parse at top; add it
import urllib.parse

since = "2026-11-25"
topics = ["dsh-plugin", "deepseek-harness", "deepseek-harness-plugin"]
found = {}  # full_name -> (desc, stars)
raw_total = 0
for topic in topics:
    page = 1
    retries = 0
    while page <= 60:
        try:
            data = github_search(topic, since, page, per_page=30)
        except urllib.error.HTTPError as e:
            if e.code == 403:
                print(f"  rate-limited on {topic} p{page}, sleeping 60s", flush=True)
                time.sleep(60)
                continue
            else:
                print(f"  HTTP {e.code} on {topic} p{page}", flush=True)
                break
        except Exception as e:
            retries += 1
            print(f"  err {e} on {topic} p{page} (retry {retries})", flush=True)
            if retries > 5:
                break
            time.sleep(5)
            continue
        retries = 0
        items = data.get("items", [])
        if not items:
            break
        raw_total += len(items)
        for it in items:
            fn = it["full_name"]
            if fn in existing or fn.lower() in existing_lower:
                continue
            found[fn] = (it.get("description") or "", it.get("stargazers_count", 0))
        print(f"  {topic} p{page}: {len(items)} items, new-candidate {len(found)}", flush=True)
        if len(items) < 30:
            break
        page += 1
        time.sleep(7)  # respect 10/min unauthenticated search limit
    # incremental save after each topic
    json.dump(found, open(os.path.join(ROOT, "_candidates.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"  [saved candidates after {topic}: {len(found)}]", flush=True)

print(f"\nraw search hits: {raw_total}, unique new candidates: {len(found)}", flush=True)
# persist candidates incrementally so progress survives interruption
json.dump(found, open(os.path.join(ROOT, "_candidates.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("wrote _candidates.json", flush=True)

# Verify root manifest for each candidate (concurrent)
import concurrent.futures as cf
def verify_one(fn):
    desc, stars = found[fn]
    owner, name = fn.split("/")
    pkg = fetch_raw(owner, name, "main") or fetch_raw(owner, name, "master")
    if has_dsh_bundle(pkg):
        return (fn, desc, stars, classify(name, desc))
    return None

verified = []
checked = 0
with cf.ThreadPoolExecutor(max_workers=24) as ex:
    futs = {ex.submit(verify_one, fn): fn for fn in found}
    for fut in cf.as_completed(futs):
        res = fut.result()
        if res:
            verified.append(res)
        checked += 1
        if checked % 200 == 0:
            print(f"  manifest-checked {checked}/{len(found)}, verified {len(verified)}", flush=True)

print(f"\nVERIFIED new DSH plugins: {len(verified)}", flush=True)
by_sec = {}
for fn, desc, stars, sec in verified:
    by_sec.setdefault(sec, []).append((fn, stars))
for sec in SECTIONS:
    lst = by_sec.get(sec, [])
    print(f"  [{sec}] {len(lst)}", flush=True)

out = [{"full_name": fn, "desc": d, "stars": s, "section": sec} for fn, d, s, sec in verified]
json.dump(out, open(os.path.join(ROOT, "_scan.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("wrote _scan.json", flush=True)
