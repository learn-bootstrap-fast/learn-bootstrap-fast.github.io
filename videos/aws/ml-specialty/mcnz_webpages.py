#!/usr/bin/env python3
import json, re
from pathlib import Path

# ========= Minimal config =========
VIDEOS_INPUT_FILE = "exam-simplified-questions-qid.json"

# Kept for populating urls in the JSON records
QUESTIONS_BASE_URL = "https://certificationation.com/questions"
VIDEOS_BASE_URL    = "https://certificationation.com/videos"

# File naming prefix (static; no folder injection)
OUTPUT_PREFIX = "exam-"

# Metadata templates (neutral)
TITLE_MAX = 60
TITLE_SUFFIX = " Exam"
DESC_MAX = 160
DESC_PREFIX = "Video for "
HEADING_TEXT = "Cloud Practitioner Exam Question Answer"

# Fixed CTA/link as requested
FIXED_LINK_URL = "https://certificationexams.pro/aws/index.html"
FIXED_LINK_TEXT = "Next Exam Question"

BACKUP_BEFORE_WRITE = True
# ==================================

def read_records(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def strip_html_tags(s: str) -> str:
    if not s:
        return ""
    s = re.sub(r"<\s*br\s*/?\s*>", " ", s, flags=re.IGNORECASE)
    s = re.sub(r"<[^>]+>", "", s)
    return s

def normalize_whitespace(s: str) -> str:
    return re.sub(r"\s+", " ", s.replace("\u00A0", " ")).strip()

def strip_trailing_punct(s: str) -> str:
    return s.rstrip(" ,;:.—–-")

def lower_first_char(s: str) -> str:
    return s[0].lower() + s[1:] if s else s

def truncate_on_word_boundary(s: str, max_len: int) -> str:
    s = s.strip()
    if len(s) <= max_len:
        return s
    cut = s.rfind(" ", 0, max_len + 1)
    return s[:cut].rstrip() if cut != -1 else s[:max_len].rstrip()

def build_title(original_query: str, title_suffix: str) -> str:
    q = normalize_whitespace(strip_html_tags(original_query))
    budget = TITLE_MAX - len(title_suffix)
    if budget <= 0:
        return title_suffix.strip()[:TITLE_MAX]
    kept, current_len = [], 0
    for w in q.split(" "):
        add_len = len(w) if not kept else 1 + len(w)
        if current_len + add_len <= budget:
            kept.append(w); current_len += add_len
        else:
            break
    base = strip_trailing_punct(" ".join(kept))
    return f"{base}{title_suffix}"

def build_description(original_query: str, desc_prefix: str) -> str:
    q = lower_first_char(normalize_whitespace(strip_html_tags(original_query)))
    return truncate_on_word_boundary(desc_prefix + q, DESC_MAX)

def yaml_escape(s: str) -> str:
    return s.replace("\r", " ").replace("\n", " ").replace('"', r'\"')

def slugify(text: str) -> str:
    return re.sub(r"-{2,}", "-", re.sub(r"[^a-z0-9]+", "-", text.lower())).strip("-") or "na"

def words_after_25_letters(original_query: str) -> str:
    cleaned = normalize_whitespace(strip_html_tags(original_query))
    if not cleaned:
        return "na"
    letter_count = 0
    letter_25_idx = None
    for i, ch in enumerate(cleaned):
        if ch.isalpha():
            letter_count += 1
            if letter_count == 25:
                letter_25_idx = i
                break
    if letter_25_idx is None:
        return slugify(cleaned)
    m = re.search(r"\s+", cleaned[letter_25_idx + 1:])
    if not m:
        return slugify(cleaned)
    start = (letter_25_idx + 1) + m.end()
    remaining = cleaned[start:].strip()
    words = remaining.split()
    if len(words) > 1 and len(words[0]) <= 2:
        words = words[1:]
    return slugify(" ".join(words[:5])) if len(words) >= 5 else slugify(cleaned)

def build_filename(idx: int, original_query: str, output_prefix: str) -> str:
    return f"{output_prefix}{words_after_25_letters(original_query)}-exam-{idx:03d}.html"

def write_record_html(
    idx: int,
    record: dict,
    outdir: Path,
    url_prefix: str,
    layout: str,
    title_suffix: str,
    desc_prefix: str
):
    original_query = record.get("originalQuery") or record.get("query") or ""
    out_filename = build_filename(idx, original_query, OUTPUT_PREFIX)
    out_path = outdir / out_filename

    title = build_title(original_query, title_suffix)
    description = build_description(original_query, desc_prefix)
    full_query_clean = normalize_whitespace(strip_html_tags(original_query))

    # File's own URL (site URL form for JSON fields)
    url_prefix = url_prefix.rstrip("/")
    full_url = f"{url_prefix}/{out_filename}" if url_prefix else out_filename

    # Sibling URL (questions site path; no folder mirroring)
    sibling_url = f"{QUESTIONS_BASE_URL.rstrip('/')}/{out_filename}"

    # Save BOTH urls back into the record
    record["video_url"] = full_url
    record["url"] = sibling_url

    # Front matter
    fm_lines = [
        "---",
        f'title: "{yaml_escape(title)}"',
        f'description: "{yaml_escape(description)}"',
        f"layout: {layout}",
        f"heading: {HEADING_TEXT}",
        f'link-text: "{FIXED_LINK_TEXT}"',
        f'link: "{FIXED_LINK_URL}"',
        f'full-query: "{yaml_escape(full_query_clean)}"',
        # Video metadata
        'video_host: "youtube"',
        'video_id: "ZYRYaPtL4WE"',
        'upload_date: "2025-10-01T11:11:11+11:11"',
        'duration: "PT1H46M27S"',
        'thumbnail_url: "https://i.ytimg.com/vi/ZYRYaPtL4WE/maxresdefault.jpg"',
        'content_url: "https://youtu.be/ZYRYaPtL4WE"',
        'embed_url: "https://www.youtube.com/embed/ZYRYaPtL4WE"',
        'publisher_name: "certificationation.com"',
        'publisher_logo: "/assets/images/logo-512.png"',
        'in_language: "en"',
        "is_accessible_for_free: true",
        "tags:",
        "  - Certification Exam",
        "  - Practice Exam",
        "  - Exam Simulator",
        "  - Real Exam Questions",
        "  - Exam Questions and Answers",
        "  - Practice test",
        "  - Real Certification Exam Questions",
        "  - Certification Exam Simulator",
        "---",
        "",
    ]

    body_json = json.dumps(record, ensure_ascii=False, indent=2)

    outdir.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        f.write("\n".join(fm_lines))
        f.write(body_json)
        f.write("\n")

def process_videos_only(input_file: str):
    in_path = Path(input_file).resolve()
    if not in_path.exists():
        print(f"[skip] Input not found: {in_path}")
        return

    out_dir = Path.cwd()  # write all HTML into the current directory
    url_prefix = VIDEOS_BASE_URL.rstrip("/")

    records = read_records(in_path)
    if not isinstance(records, list):
        raise SystemExit(f"Input JSON must be an array of records: {in_path}")

    for i, rec in enumerate(records, start=1):
        write_record_html(
            i,
            rec,
            out_dir,
            url_prefix,
            layout="video",
            title_suffix=TITLE_SUFFIX.replace("  ", " ").strip(),
            desc_prefix=DESC_PREFIX
        )

    if BACKUP_BEFORE_WRITE:
        bak_path = in_path.with_suffix(in_path.suffix + ".bak")
        bak_path.write_text(in_path.read_text(encoding="utf-8"), encoding="utf-8")

    in_path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[videos] Wrote {len(records)} files to {out_dir}")
    print(f"Updated {in_path} with 'url' and 'video_url' for each record")

def main():
    process_videos_only(VIDEOS_INPUT_FILE)

if __name__ == "__main__":
    main()
