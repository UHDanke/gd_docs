"""
populate_sidebar.py
====================
Scans a docs folder for Markdown files and syncs them into the sidebar CSV.

- Existing rows are preserved as-is (including their Exclude value).
- New entries not already in the CSV are appended with Exclude=TRUE.
- Rows in the CSV whose link no longer exists on disk are left untouched
  (so you can decide whether to remove them manually).

Usage:
    python populate_sidebar.py                        # docs/ and sidebar.csv in cwd
    python populate_sidebar.py --docs path/to/docs
    python populate_sidebar.py --csv  path/to/sidebar.csv
    python populate_sidebar.py --docs docs/ --csv sidebar.csv
"""

import argparse
import csv
import os
from pathlib import Path


FIELDNAMES = ["Section", "Subsection", "Text", "Link", "Exclude"]


def path_to_parts(rel: Path) -> tuple[str, str, str, str]:
    """
    Convert a relative .md path to (Section, Subsection, Text, Link).

    docs/triggers/audio/bpm_guide.md
      → Section=Triggers, Subsection=Audio, Text=Bpm Guide, Link=/triggers/audio/bpm_guide

    docs/editor/autobuild.md
      → Section=Editor, Subsection='', Text=Autobuild, Link=/editor/autobuild

    docs/to_do_list.md
      → Section='', Subsection='', Text=To Do List, Link=/to_do_list
    """
    parts = rel.with_suffix("").parts  # drop .md

    def title(s: str) -> str:
        return s.replace("_", " ").title()

    if len(parts) == 1:
        # top-level file → no section (bare top-level item)
        return ("", "", title(parts[0]), f"/{parts[0]}")

    if len(parts) == 2:
        section, page = parts
        return (title(section), "", title(page), f"/{section}/{page}")

    if len(parts) == 3:
        section, subsection, page = parts
        return (
            title(section),
            title(subsection),
            title(page),
            f"/{section}/{subsection}/{page}",
        )

    # Deeper nesting: flatten extras into subsection label
    section = parts[0]
    subsection = "/".join(parts[1:-1])
    page = parts[-1]
    link = "/" + "/".join(parts)
    return (title(section), title(subsection), title(page), link)


def load_csv(csv_path: Path) -> tuple[dict[str, dict], list[str]]:
    """Return (rows_by_link, ordered_links)."""
    rows_by_link: dict[str, dict] = {}
    ordered_links: list[str] = []

    if not csv_path.exists():
        return rows_by_link, ordered_links

    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            link = row["Link"]
            rows_by_link[link] = row
            ordered_links.append(link)

    return rows_by_link, ordered_links


def scan_docs(docs_dir: Path) -> list[tuple[str, str, str, str]]:
    """Return list of (Section, Subsection, Text, Link) for every .md file found."""
    entries = []
    for md_file in sorted(docs_dir.rglob("*.md")):
        rel = md_file.relative_to(docs_dir)
        entries.append(path_to_parts(rel))
    return entries


def main():
    parser = argparse.ArgumentParser(description="Sync docs folder into sidebar CSV.")
    parser.add_argument("--docs", default="docs", help="Path to docs folder (default: ./docs)")
    parser.add_argument("--csv",  default=".data/sidebar.csv", help="Path to sidebar CSV (default: ./.data/sidebar.csv)")
    args = parser.parse_args()

    docs_dir = Path(args.docs)
    csv_path = Path(args.csv)

    if not docs_dir.is_dir():
        raise SystemExit(f"Error: docs folder not found: {docs_dir}")

    rows_by_link, ordered_links = load_csv(csv_path)

    doc_entries = scan_docs(docs_dir)
    if not doc_entries:
        raise SystemExit(f"No .md files found under {docs_dir}")

    doc_links = {link for _, _, _, link in doc_entries}

    # Mark rows whose file no longer exists as excluded
    deleted = 0
    for link, row in rows_by_link.items():
        if link not in doc_links and row["Exclude"].strip().upper() != "TRUE":
            row["Exclude"] = "TRUE"
            deleted += 1

    # Append new entries
    added = 0
    for section, subsection, text, link in doc_entries:
        if link not in rows_by_link:
            rows_by_link[link] = {
                "Section":    section,
                "Subsection": subsection,
                "Text":       text,
                "Link":       link,
                "Exclude":    "TRUE",   # new entries excluded by default
            }
            ordered_links.append(link)
            added += 1

    # Write back, preserving original order + new entries at the end
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        for link in ordered_links:
            writer.writerow(rows_by_link[link])

    total = len(ordered_links)
    print(f"Done. {added} new row(s) added, {deleted} deleted row(s) excluded. {total} total rows in {csv_path}.")


if __name__ == "__main__":
    main()
