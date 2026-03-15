import csv
import sys


COLUMNS = [
    "Category", "Fixed", "Excluded", "Version", "Date", "Platform",
    "Short Description", "Long Description", "Suggestions", "Workarounds",
    "Video", "Level ID"
]

META_FIELDS = ["Version", "Date", "Platform", "Level ID"]


def normalize(val):
    return " ".join(val.strip().split())


def csv_to_md(csv_path, md_path):
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Normalize all values
    cleaned = []
    for row in rows:
        cleaned.append({k: normalize(row.get(k, "")) for k in COLUMNS})

    # Group by category
    categories = {}
    for row in cleaned:
        cat = row["Category"] or "Uncategorized"
        categories.setdefault(cat, []).append(row)

    lines = []
    for cat in sorted(categories.keys()):
        lines.append(f"# {cat}")
        lines.append("")
        for entry in categories[cat]:
            excluded = entry["Excluded"].upper() == "TRUE"
            fixed = entry["Fixed"].upper() == "TRUE"
            short_desc = entry["Short Description"]

            prefix = "[FIXED] " if fixed else ""
            excluded_tag = " ~~EXCLUDED~~" if excluded else ""
            lines.append(f"## {prefix}{short_desc}{excluded_tag}")
            lines.append("")

            for field in META_FIELDS:
                val = entry[field]
                if val:
                    lines.append(f"**{field}:** {val}")
            lines.append("")

            long_desc = entry["Long Description"]
            if long_desc:
                lines.append("### Description")
                lines.append(long_desc)
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

    # Single trailing newline, no trailing whitespace
    output = "\n".join(lines).rstrip() + "\n"

    with open(md_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(output)

    included = sum(1 for r in cleaned if r["Excluded"].upper() != "TRUE")
    excluded_count = len(cleaned) - included
    print(f"✅ Converted '{csv_path}' → '{md_path}' ({included} included, {excluded_count} excluded)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python bugs_from_csv.py input.csv output.md")
        sys.exit(1)
    csv_to_md(sys.argv[1], sys.argv[2])
