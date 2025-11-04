#!/usr/bin/env python3
"""
Replace a specific upload_date in all .html/.htm files under the current directory.

Search:
  upload_date: "2025-10-01T11:11:11+11:11"

Replace with:
  upload_date: "2025-11-05T00:00:00Z"
"""

from pathlib import Path

SEARCH = 'upload_date: "2025-10-01T11:11:11+11:11"'
REPLACE = 'upload_date: "2025-11-05T00:00:00Z"'
EXTS = {".html", ".htm"}

def main():
    root = Path(".")
    changed = 0
    scanned = 0

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in EXTS:
            continue

        scanned += 1
        try:
            text = path.read_text(encoding="utf-8", errors="strict")
        except UnicodeDecodeError:
            # Fallback if some files have odd encodings
            text = path.read_text(encoding="utf-8", errors="ignore")

        if SEARCH in text:
            new_text = text.replace(SEARCH, REPLACE)
            if new_text != text:
                # Make a backup once per file before writing (with .bak extension)
                bak = path.with_suffix(path.suffix + ".bak")
                if not bak.exists():
                    bak.write_text(text, encoding="utf-8", errors="ignore")

                path.write_text(new_text, encoding="utf-8", errors="ignore")
                changed += 1
                print(f"Updated: {path}")

    print(f"\nScanned files: {scanned}")
    print(f"Updated files: {changed}")

if __name__ == "__main__":
    main()
