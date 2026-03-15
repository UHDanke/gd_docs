import csv
import sys
import os
import re
from datetime import datetime


COLUMNS = [
    "Category", "Fixed", "Exclude", "Version", "Date", "Platform",
    "Short Description", "Long Description", "Examples", "Suggestions", "Workarounds",
    "Video", "Level ID"
]

META_FIELDS = ["Fixed", "Version", "Date", "Platform", "Level ID"]


def normalize(val):
    return " ".join(val.strip().split())


def category_to_filename(cat):
    return re.sub(r'[^a-z0-9]+', '_', cat.lower()).strip('_') + ".md"


def format_date(val):
    if not val:
        return ""
    # Try common formats
    for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%m/%d/%Y"):
        try:
            return datetime.strptime(val, fmt).strftime("%d/%m/%Y")
        except ValueError:
            pass
    # Try parsing the long JS date string e.g. "Thu Dec 18 2025 00:00:00 GMT+0200 (...)"
    try:
        return datetime.strptime(val[:15].strip(), "%a %b %d %Y").strftime("%d/%m/%Y")
    except ValueError:
        pass
    return val  # fallback: return as-is


def entry_to_lines(entry):
    lines = []
    excluded = entry["Exclude"].upper() == "TRUE"
    fixed = entry["Fixed"].upper() == "TRUE"
    short_desc = entry["Short Description"]

    prefix = "[FIXED] " if fixed else ""
    excluded_tag = " ~~EXCLUDED~~" if excluded else ""
    lines.append(f"## {prefix}{short_desc}{excluded_tag}")
    lines.append("")

    for field in META_FIELDS:
        val = entry[field]
        if field == "Date":
            val = format_date(val)
        if field == "Fixed":
            # Always emit Fixed so it survives roundtrip; heading tag is visual-only
            lines.append(f"**{field}:** {val}  ")
        elif val:
            lines.append(f"**{field}:** {val}  ")
    lines.append("")

    long_desc = entry["Long Description"]
    if long_desc:
        lines.append("### Description")
        lines.append(long_desc)
        lines.append("")

    examples = entry["Examples"]
    if examples:
        lines.append("### Examples")
        lines.append(examples)
        lines.append("")

    suggestions = entry["Suggestions"]
    if suggestions:
        lines.append("### Suggestions")
        lines.append(suggestions)
        lines.append("")

    workarounds = entry["Workarounds"]
    if workarounds:
        lines.append("### Workarounds")
        lines.append(workarounds)
        lines.append("")

    video = entry["Video"]
    if video:
        lines.append("### Video")
        lines.append(video)
        lines.append("")

    return lines


def csv_to_md(csv_path, output_dir):
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    cleaned = []
    for row in rows:
        cleaned.append({k: normalize(row.get(k, "")) for k in COLUMNS})

    # Group by category
    categories = {}
    for row in cleaned:
        cat = row["Category"] or "Uncategorized"
        categories.setdefault(cat, []).append(row)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Clear existing .md files except README.md
    for fname in os.listdir(output_dir):
        if fname.endswith(".md") and fname.lower() != "readme.md":
            os.remove(os.path.join(output_dir, fname))

    # Write one file per category (excluded entries omitted from MD)
    for cat in sorted(categories.keys()):
        entries = [e for e in categories[cat] if e["Exclude"].upper() != "TRUE"]
        if not entries:
            continue
        lines = [f"# {cat}", ""]
        for entry in entries:
            lines.extend(entry_to_lines(entry))

        output = "\n".join(lines).rstrip() + "\n"
        fname = category_to_filename(cat)
        with open(os.path.join(output_dir, fname), "w", encoding="utf-8", newline="\n") as f:
            f.write(output)

    included = sum(1 for r in cleaned if r["Exclude"].upper() != "TRUE")
    excluded_count = len(cleaned) - included
    print(f"Converted '{csv_path}' → '{output_dir}/' ({len(categories)} files, {included} included, {excluded_count} excluded)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python bugs_from_csv.py input.csv output_dir/")
        sys.exit(1)
    csv_to_md(sys.argv[1], sys.argv[2])
