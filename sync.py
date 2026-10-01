import os, time, requests
from pathlib import Path

SESSION = os.environ["LEETCODE_SESSION"]
CSRF = os.environ["LEETCODE_CSRF"]

EXT = {
    "python": "py", "python3": "py", "cpp": "cpp", "java": "java",
    "c": "c", "javascript": "js", "typescript": "ts", "golang": "go",
    "rust": "rs", "csharp": "cs", "kotlin": "kt", "swift": "swift",
    "mysql": "sql", "postgresql": "sql", "oraclesql": "sql",
}

headers = {
    "Cookie": f"LEETCODE_SESSION={SESSION}; csrftoken={CSRF}",
    "x-csrftoken": CSRF,
    "Referer": "https://leetcode.com/submissions/",
    "User-Agent": "Mozilla/5.0",
}

seen = set()   # (slug, lang) -> keep only the newest accepted solution
saved = 0
offset = 0

while True:
    r = requests.get(
        f"https://leetcode.com/api/submissions/?offset={offset}&limit=20",
        headers=headers, timeout=30,
    )
    r.raise_for_status()
    data = r.json()

    for s in data.get("submissions_dump", []):
        if s["status_display"] != "Accepted":
            continue
        key = (s["title_slug"], s["lang"])
        if key in seen:
            continue
        seen.add(key)

        ext = EXT.get(s["lang"], "txt")
        folder = Path("problems") / s["title_slug"]
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / f"solution.{ext}"

        code = s["code"].replace("\r\n", "\n")
        if not path.exists() or path.read_text() != code:
            path.write_text(code)
            saved += 1

    if not data.get("has_next"):
        break
    offset += 20
    time.sleep(1.5)   # be polite, avoid rate limits

print(f"Updated {saved} file(s)")
