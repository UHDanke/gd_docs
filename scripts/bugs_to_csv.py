import csv
import os
import sys


COLUMNS = [
    "Category", "Fixed", "Exclude", "Version", "Date", "Platform",
    "Short Description", "Long Description", "Examples", "Suggestions", "Workarounds",
    "Video", "Level ID"
]

META_FIELDS = {"Version", "Date", "Platform", "Level ID"}


def normalize(val):
    return " ".join(val.strip().split())


def parse_md(md_path):
    with open(md_path, encoding="utf-8") as f:
        lines = f.readlines()

    entries = []
    current_category = None
    current_entry = None
    current_section = None

    for line in lines:
        stripped = line.rstrip()

        # Category (h1)
        if stripped.startswith("# ") and not stripped.startswith("## "):
            current_category = normalize(stripped[2:])
            current_entry = None
            current_section = None

        # Entry (h2)
        elif stripped.startswith("## "):
            if current_entry:
                entries.append(current_entry)
            title = normalize(stripped[3:])
            # Strip visual-only tags to get the clean short description
            fixed = "TRUE" if "[FIXED]" in title else "FALSE"
            short_desc = title.replace("[FIXED]", "").strip()
            current_entry = {
                "Category": current_category or "",
                "Fixed": fixed,      # derived from [FIXED] heading tag
                "Exclude": "FALSE",  # overwritten by in-place merge
                "Version": "",
                "Date": "",
                "Platform": "",
                "Short Description": short_desc,
                "Long Description": "",
                "Examples": "",
                "Suggestions": "",
                "Workarounds": "",
                "Video": "",
                "Level ID": "",
            }
            current_section = None

        # Section headers (h3)
        elif stripped.startswith("### "):
            current_section = normalize(stripped[4:])

        # Metadata bold fields: **Key:** Value
        elif stripped.startswith("**") and ":**" in stripped and current_entry:
            try:
                key, val = stripped.split(":**", 1)
                key = key.lstrip("*").strip()
                val = normalize(val)
                if key in META_FIELDS:
                    current_entry[key] = val
            except ValueError:
                pass

        # Section content
        elif current_entry and current_section and stripped:
            field_map = {
                "Description": "Long Description",
                "Examples": "Examples",
                "Suggestions": "Suggestions",
                "Workarounds": "Workarounds",
                "Video": "Video",
            }
            field = field_map.get(current_section)
            if field:
                existing = current_entry.get(field, "")
                new_val = normalize(stripped)
                current_entry[field] = (existing + " " + new_val).strip() if existing else new_val

    if current_entry:
        entries.append(current_entry)

    return entries


def load_csv(csv_path):
    """Return existing rows keyed by (Category, Short Description)."""
    existing = {}
    if not os.path.exists(csv_path):
        return existing
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            key = (normalize(row.get("Category", "")), normalize(row.get("Short Description", "")))
            existing[key] = row
    return existing


def md_to_csv(md_path, csv_path):
    entries = parse_md(md_path)
    existing = load_csv(csv_path)

    merged = []
    added = 0
    for entry in entries:
        key = (entry["Category"], entry["Short Description"])
        if key in existing:
            # Preserve only Exclude from the existing CSV; re-derive everything else from MD
            entry["Exclude"] = normalize(existing[key].get("Exclude", "FALSE"))
        else:
            # New entries (not previously in CSV) default to excluded
            entry["Exclude"] = "TRUE"
            added += 1
        merged.append(entry)

    with open(csv_path, "w", newline="\n", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(merged)

    dropped = len(existing) - (len(merged) - added)
    included = sum(1 for e in merged if e["Exclude"].upper() != "TRUE")
    excluded_count = len(merged) - included
    print(f"Converted '{md_path}' → '{csv_path}' ({added} added, {dropped} dropped, {included} included, {excluded_count} excluded)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python bugs_to_csv.py input.md output.csv")
        sys.exit(1)
    md_to_csv(sys.argv[1], sys.argv[2])
