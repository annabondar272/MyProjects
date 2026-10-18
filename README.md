# MyProjects

כספת [Obsidian](https://obsidian.md) לניהול ותיעוד הפרויקטים שלי, בעבודה משותפת עם [Claude Code](https://claude.com/claude-code).

## מבנה

```
MyProjects/
├── פרויקטים/
│   └── <שם הפרויקט>/
│       ├── סקירת הפרויקט.md   # מטרה, קישורים, מבנה, משימות פתוחות והיסטוריה
│       └── יומן פעולות.md     # נכתב אוטומטית ע"י ה-Hook
├── .claude/
│   ├── settings.json          # הגדרת ה-Hook
│   └── hooks/obsidian_log.py  # סקריפט התיעוד
├── .obsidian/                 # הגדרות הכספת
└── CLAUDE.md                  # הנחיות עבודה ל-Claude Code
```

## פרויקטים

| פרויקט | תיאור | סטטוס |
|---|---|---|
| [חנות בגדי ילדים](פרויקטים/חנות%20בגדי%20ילדים/סקירת%20הפרויקט.md) | אתר תדמית לחנות בגדי ילדים עם משלוחים לכל הארץ | בעבודה |

## תיעוד אוטומטי

Hook מסוג `PostToolUse` רץ אחרי כל פעולה של Claude Code ומוסיף שורה (תאריך, כלי, פרטים) ל`יומן פעולות.md` של הפרויקט. פעולות קריאה וחיפוש לא נרשמות.

בדיקה ידנית:

```bash
echo '{"tool_name":"Bash","tool_input":{"description":"test"}}' | python .claude/hooks/obsidian_log.py
```

## דרישות

- [Obsidian](https://obsidian.md) עם התוסף [Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) (לחיבור Claude Code דרך MCP)
- Python 3 (עבור ה-Hook)
- [Claude Code](https://claude.com/claude-code)

## תהליך עבודה

כל משימה עוברת: תכנון (Opus) ← ביצוע (Sonnet) ← בדיקות E2E, מקרי קצה ורגרסיה ← בדיקת אבטחה. הפירוט המלא ב-[CLAUDE.md](CLAUDE.md).
