"""PostToolUse hook: append a line to the Obsidian action log for every agent action."""
import json
import sys
from datetime import datetime
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
LOG = VAULT / "פרויקטים" / "חנות בגדי ילדים" / "יומן פעולות.md"

# Read-only / bookkeeping tools that are not "actions"
SKIP = {"Read", "Glob", "Grep", "ToolSearch", "Skill", "ListAgents"}


def summarize(tool, inp):
    if tool in ("Write", "Edit", "NotebookEdit"):
        return f"`{inp.get('file_path', '')}`"
    if tool in ("Bash", "PowerShell"):
        desc = inp.get("description") or inp.get("command", "")
        return desc.replace("\n", " ")[:200]
    if tool == "Artifact":
        return f"{inp.get('action', 'publish')} {inp.get('file_path') or inp.get('url') or ''}".strip()
    if tool == "Agent":
        return inp.get("description", "")
    for key in ("filepath", "file_path", "path", "url", "query", "description"):
        if inp.get(key):
            return str(inp[key])[:200]
    return ""


def main():
    data = json.loads(sys.stdin.buffer.read().decode("utf-8"))
    tool = data.get("tool_name", "")
    if tool in SKIP:
        return
    # Don't log writes to the log itself
    inp = data.get("tool_input") or {}
    if "יומן פעולות" in json.dumps(inp, ensure_ascii=False):
        return

    LOG.parent.mkdir(parents=True, exist_ok=True)
    if not LOG.exists():
        LOG.write_text(
            "# יומן פעולות\n\nתיעוד אוטומטי של כל פעולה ש-Claude Code מבצע. חזרה ל-[[סקירת הפרויקט]].\n\n"
            "| תאריך ושעה | כלי | פרטים |\n|---|---|---|\n",
            encoding="utf-8",
        )
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    details = summarize(tool, inp).replace("|", "\\|")
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"| {stamp} | {tool} | {details} |\n")


if __name__ == "__main__":
    main()
