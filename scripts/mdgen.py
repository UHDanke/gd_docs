"""
mdgen.py — in-place markdown generator

Supported tags:
    <!-- @csv: path/to/file.csv -->
    ...existing content replaced on each run...
    <!-- @end -->

Usage:
    python mdgen.py                  # process all .md files in current dir
    python mdgen.py docs/            # process all .md files under docs/ recursively
    python mdgen.py file.md          # process a single file
"""

import csv
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Generators
# ---------------------------------------------------------------------------

def csv_to_markdown(csv_path: str) -> str:
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    if not rows:
        return ""

    headers = rows[0]
    col_widths = [len(h) for h in headers]
    for row in rows[1:]:
        for i, cell in enumerate(row):
            if i < len(col_widths):
                col_widths[i] = max(col_widths[i], len(cell))

    def fmt_row(cells):
        padded = list(cells) + [""] * (len(headers) - len(cells))
        return "| " + " | ".join(padded[i].ljust(col_widths[i]) for i in range(len(headers))) + " |"

    separator = "| " + " | ".join("-" * w for w in col_widths) + " |"
    lines = [fmt_row(headers), separator] + [fmt_row(r) for r in rows[1:]]
    return "\n".join(lines)


# Map tag names to handler functions.
# Each handler receives the argument string and returns a markdown string.
GENERATORS = {
    "csv": csv_to_markdown,
}


# ---------------------------------------------------------------------------
# Processor
# ---------------------------------------------------------------------------

# Matches: <!-- @tag: argument --> ... <!-- @end -->
BLOCK_RE = re.compile(
    r"(<!-- @(\w+):\s*(.+?)\s*-->)"   # opening tag  (group 1, 2, 3)
    r"(.*?)"                            # existing content (group 4)
    r"(<!-- @end -->)",                 # closing tag  (group 5)
    re.DOTALL,
)


def process_text(text: str) -> tuple[str, int]:
    """Replace all generator blocks in *text*. Returns (new_text, replacements_made)."""
    count = 0
    errors = []

    def replace(m: re.Match) -> str:
        noncount = count  # captured by closure below
        open_tag, tag, arg, _old_content, close_tag = m.groups()

        if tag not in GENERATORS:
            errors.append(f"Unknown tag '@{tag}'")
            return m.group(0)

        # Resolve relative paths relative to cwd (project root)
        resolved_arg = str(Path.cwd() / arg.strip()) if not Path(arg.strip()).is_absolute() else arg.strip()

        try:
            generated = GENERATORS[tag](resolved_arg)
        except Exception as e:
            errors.append(f"@{tag}: {e}")
            return m.group(0)

        return f"{open_tag}\n{generated}\n{close_tag}"

    new_text = BLOCK_RE.sub(replace, text)

    # Count how many blocks were actually updated
    count = len(BLOCK_RE.findall(text))

    if errors:
        for err in errors:
            print(f"  [error] {err}", file=sys.stderr)

    return new_text, count


def process_file(md_path: Path) -> None:
    text = md_path.read_text(encoding="utf-8")
    new_text, count = process_text(text)

    if count == 0:
        print(f"  (no generator blocks found)")
        return

    if new_text == text:
        print(f"  (no changes)")
        return

    md_path.write_text(new_text, encoding="utf-8")
    print(f"  updated {count} block(s)")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    args = sys.argv[1:]

    # If the first argument is an existing directory, recurse into it.
    # Otherwise treat all arguments as explicit file paths.
    if args and Path(args[0]).is_dir():
        root = Path(args[0])
        files = sorted(root.glob("**/*.md"))
        if not files:
            print(f"No .md files found under {root}")
            return
    elif args:
        files = [Path(a) for a in args]
        for f in files:
            if not f.exists():
                print(f"[skip] {f} — file not found", file=sys.stderr)
    else:
        files = sorted(Path(".").glob("**/*.md"))
        if not files:
            print("No .md files found in current directory.")
            return

    for md_file in files:
        print(f"{md_file}")
        process_file(md_file)


if __name__ == "__main__":
    main()
