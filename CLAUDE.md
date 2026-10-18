# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

An Obsidian vault (notes in Markdown), not a software project. There is no build, lint, or test tooling. The user writes in Hebrew; note names, folders and content are Hebrew, and replies should be in Hebrew unless the user writes in English.

## Required workflow (every task)

1. **Plan before executing.** Never start making changes without a plan. Planning is done with **Opus 5.5** (`claude-opus-5-5`): enter plan mode, or use the `Plan` agent with `model: "opus"`. Present the plan before executing it.
2. **Execute with Sonnet 5.5** (`claude-sonnet-5-5`). Delegate the implementation to an `Agent` with `model: "sonnet"`, passing it the approved plan.
3. **After every execution, test:**
   - **E2E tests:** run the result end to end the way a user would (for a web page, open it in the browser and go through every section, link and button).
   - **Edge cases:** long or empty content, Hebrew/RTL mixed with English and numbers, phone width, dark mode, missing data.
   - **Regression:** confirm that things that worked before the change still work.
4. **Security review after any code is written:** run `/security-review`, or review the change for XSS, unsafe input handling, secrets in code, external scripts not pinned to a version, and unsafe links.
5. Report the test and review results honestly, including anything that failed or was skipped.

## Layout

- `פרויקטים/<project name>/` holds one folder per project. Each one has:
  - `סקירת הפרויקט.md`: the project overview, with frontmatter (`project`, `status`, `created`, `tags`), links, structure, a checklist of open items, and a dated history section.
  - `יומן פעולות.md`: an automatic action log written by the hook below. Don't edit it by hand.
- `.obsidian/`: vault config. `workspace*.json` and the REST API plugin's `data.json` (which holds its API key) are gitignored. Don't commit them.

## Working with the vault

- Read and write notes through the `mcp__obsidian__*` tools, which talk to the vault through the `obsidian-local-rest-api` plugin. Obsidian must be running for them to work. Direct file edits also work, because the vault is this directory.
- Use Obsidian conventions: `[[wikilinks]]` between notes, YAML frontmatter, and `- [ ]` checkboxes.
- When doing project work, update that project's `סקירת הפרויקט.md`: add a dated line to its history and tick off or add checklist items.

## Action-log hook

`.claude/settings.json` registers a `PostToolUse` hook (matcher `*`) that runs `python .claude/hooks/obsidian_log.py`. The script appends one table row (timestamp | tool | details) to the log file path hardcoded in its `LOG` constant, which currently points to `פרויקטים/חנות בגדי ילדים/יומן פעולות.md`. Read-only tools listed in `SKIP` aren't logged, and nor are actions that touch the log itself. When starting a new project, change `LOG` to that project's folder.

Test the hook manually:
```
echo '{"tool_name":"Bash","tool_input":{"description":"test"}}' | python .claude/hooks/obsidian_log.py
```

## Projects

- **חנות בגדי ילדים** (kids' clothing store site): a single-file HTML page in Hebrew, right to left, published as a claude.ai Artifact. The overview note has the artifact URL. The HTML source currently lives only in a session scratchpad (temporary), so to change the site, read the artifact back with the Artifact tool's `read` action and republish to the same URL.
