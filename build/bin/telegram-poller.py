#!/usr/bin/env python3
"""PavOS Telegram two-way (v1.5). One chat only. Read-only MCP; no sends."""
import fcntl, json, os, subprocess, time, urllib.parse, urllib.request, uuid, datetime
HOME = "/home/pavlos"; VAULT = f"{HOME}/pavos-style"
env = dict(l.strip().split("=", 1) for l in open(f"{HOME}/.pavos-style.env") if "=" in l)
TOKEN, CHAT = env["TELEGRAM_TOKEN"], int(env["TELEGRAM_CHAT_ID"])
API = f"https://api.telegram.org/bot{TOKEN}/"
LOGDIR = f"{VAULT}/build/logs"; os.makedirs(LOGDIR, exist_ok=True)
OFFSET_F, SESSION_F, LOG_F = f"{LOGDIR}/tg.offset", f"{LOGDIR}/tg.session", f"{LOGDIR}/telegram.log"
ALLOW = ("Read,Glob,Grep,Edit,Write,WebSearch,WebFetch,Bash(git add:*),Bash(git commit:*),Bash(git log:*),Bash(git status:*),Bash(date:*),Bash(ls:*),Bash(cat:*),"
 "mcp__claude_ai_Gmail__search_threads,mcp__claude_ai_Gmail__get_thread,mcp__claude_ai_Gmail__get_message,mcp__claude_ai_Gmail__list_labels,"
 "mcp__claude_ai_Google_Calendar__list_calendars,mcp__claude_ai_Google_Calendar__list_events,mcp__claude_ai_Google_Calendar__get_event,mcp__claude_ai_Google_Calendar__create_event,mcp__claude_ai_Google_Calendar__update_event,mcp__claude_ai_Google_Calendar__delete_event,"
 "mcp__claude_ai_Google_Drive__search_files,mcp__claude_ai_Google_Drive__download_file_content,mcp__claude_ai_Google_Drive__get_file_metadata")
DENY = ("mcp__claude_ai_Gmail__send_message,mcp__claude_ai_Gmail__reply,mcp__claude_ai_Gmail__forward,mcp__claude_ai_Gmail__create_draft,mcp__claude_ai_Gmail__update_draft,mcp__claude_ai_Gmail__trash_message,mcp__claude_ai_Gmail__trash_thread,"
 ""
 "mcp__claude_ai_Google_Drive__create_file,mcp__claude_ai_Google_Drive__update_file,mcp__claude_ai_Google_Drive__trash_file,mcp__claude_ai_Google_Drive__share_file,Bash(git push:*),Bash(curl:*),Bash(rm:*)")
ENV = dict(os.environ, HOME=HOME, PATH=f"{HOME}/.local/bin:/usr/local/bin:/usr/bin:/bin", TZ="Europe/London")

def api(method, **kw):
    data = urllib.parse.urlencode(kw).encode()
    with urllib.request.urlopen(API + method, data=data, timeout=70) as r: return json.load(r)
def log(kind, text):
    with open(LOG_F, "a") as f: f.write(f"{datetime.datetime.now():%F %T} {kind}: {text.replace(chr(10),' / ')[:2000]}\n")
def send(text):
    text = text.strip() or "(empty reply)"
    for i in range(0, len(text), 3900): api("sendMessage", chat_id=CHAT, text=text[i:i+3900])
def rf(p, d=""): return open(p).read().strip() if os.path.exists(p) else d
LOCK = "/home/pavlos/.lock-pavos-style"
def with_lock(fn):
    fh = open(LOCK, "w")
    for _ in range(10):
        try: fcntl.flock(fh, fcntl.LOCK_EX | fcntl.LOCK_NB); break
        except BlockingIOError: time.sleep(0.5)
    else:
        send("A scheduled run is in progress — I'll answer as soon as it finishes."); fcntl.flock(fh, fcntl.LOCK_EX)
    try: return fn()
    finally: fcntl.flock(fh, fcntl.LOCK_UN); fh.close()
def ask(text):
    now = datetime.datetime.now().strftime("%a %d %b %H:%M")
    prompt = (f"Telegram message from Pavlos, {now} Europe/London. Reply in plain text, no markdown, under 3500 characters. "
              "Follow CLAUDE.md. Pre-graduation: no sends; if a send would be the right action, describe it under 'Ready to send'. "
              "If he names a day type or asks what to wear, answer from wiki/04-looks.md first. If he says picked N or worn, log it in wiki/03-state.md. If it is a catalogue fact or a photo, apply 02a-schema provenance rules and edit data/02-wardrobe.csv. Always: one log line, git commit. "
              f"Message: {text}")
    sid = rf(SESSION_F)
    base = ["claude", "-p", prompt, "--allowedTools", ALLOW, "--disallowedTools", DENY, "--permission-mode", "acceptEdits", "--output-format", "text"]
    if sid:
        r = subprocess.run(base + ["--resume", sid], cwd=VAULT, env=ENV, capture_output=True, text=True, timeout=600)
        if r.returncode == 0: return r.stdout
        log("resume-failed", r.stderr)
    sid = str(uuid.uuid4()); open(SESSION_F, "w").write(sid)
    r = subprocess.run(base + ["--session-id", sid], cwd=VAULT, env=ENV, capture_output=True, text=True, timeout=600)
    return r.stdout if r.returncode == 0 else f"PavOS error (rc={r.returncode}): {r.stderr[-800:]}"

offset = int(rf(OFFSET_F, "0") or 0)
log("start", f"poller up, offset {offset}")
while True:
    try:
        upd = api("getUpdates", timeout=50, offset=offset)
    except Exception as e:
        log("poll-error", str(e)); time.sleep(5); continue
    for u in upd.get("result", []):
        offset = u["update_id"] + 1; open(OFFSET_F, "w").write(str(offset))
        m = u.get("message") or {}; text = m.get("text", "")
        if m.get("photo") or m.get("document"):
            try:
                f = (m.get("photo") or [None])[-1] or m.get("document")
                info = api("getFile", file_id=f["file_id"])["result"]["file_path"]
                ext = os.path.splitext(info)[1] or ".jpg"; pdir = f"{VAULT}/data/photos"; os.makedirs(pdir, exist_ok=True)
                dest = f"{pdir}/{datetime.datetime.now():%Y-%m-%d-%H%M%S}{ext}"
                urllib.request.urlretrieve(f"https://api.telegram.org/file/bot{TOKEN}/{info}", dest)
                text = f"[Photo saved at {dest} — open it with the Read tool and look at it.] " + (m.get("caption") or "")
            except Exception as e:
                log("photo-error", str(e)); text = "[A photo arrived but could not be saved.] " + (m.get("caption") or "")
        if m.get("chat", {}).get("id") != CHAT: log("rejected", f"chat {m.get('chat',{}).get('id')}"); continue
        if not text: continue
        log("in", text)
        if text.strip().lower() == "/status":
            send(subprocess.run([f"{VAULT}/build/bin/healthcheck.sh"], capture_output=True, text=True).stdout); continue
        if text.strip().lower().startswith("/judge"):
            arg = text.strip().split(None, 1)[1].lower() if len(text.split()) > 1 else "brief"
            skill = {"brief":"morning-brief","close":"evening-close","sysreview":"system-review","review":"weekly-review"}.get(arg, arg)
            text = (f"JUDGE the most recent run of skills/{skill}/. Read skills/{skill}/eval.md, the last row of skills/{skill}/runs.md, "
                    f"the run's output file (briefs/ for morning-brief, build/logs/ for close and sysreview), wiki/log.md and git log -3. "
                    "Walk every numbered check in eval.md: one line each, PASS or FAIL, with the artifact (file, line, commit) as evidence. "
                    "Then one line: PROPOSED VERDICT: PASS or FAIL, and the consecutive-PASS count it would make. Do NOT write anything yet. "
                    "End with: Reply AGREE to record it, or FAIL <reason> to overrule. When he replies AGREE, write the verdict into the result column "
                    "of that runs.md row, add a dated line to corrections.md if anything was noted, commit 'eval: <skill> <date> <verdict>', and confirm in one line. "
                    "If the count reaches 3, say so and name build/bin/graduate.sh — do not run it.")
        if text.strip().lower() == "/new":
            if os.path.exists(SESSION_F): os.remove(SESSION_F)
            send("New session."); continue
        try: api("sendChatAction", chat_id=CHAT, action="typing")
        except Exception: pass
        try: reply = with_lock(lambda: ask(text))
        except subprocess.TimeoutExpired: reply = "PavOS: timed out after 10 minutes."
        log("out", reply); send(reply)
