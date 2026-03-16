"""
In-place markdown generator

Tag syntax
----------
The colon and positional argument are both optional.
Keyword arguments use --key value or bare --flag (implicitly true).

    <!-- @tag -->                              no argument
    <!-- @tag: positional -->                  positional arg only
    <!-- @tag --key value -->                  keyword args only
    <!-- @tag: positional --key value -->      positional + keyword args
    <!-- @tag --flag -->                       boolean flag (value = "true")

Supported tags
--------------
    <!-- @csv: path/to/file.csv -->
    ...existing content replaced on each run...
    <!-- @end -->

    <!-- @sort_lines -->                                      sort block content in-place
    <!-- @sort_lines: path/to/file.txt -->                    sort lines from a file
    <!-- @sort_lines --reverse -->                            reverse sort, in-place
    <!-- @sort_lines: file.txt --reverse --key upper -->      reverse sort from file, case-insensitive
    <!-- @end -->

Usage
-----
    python mdgen.py                  # process all .md files in current dir
    python mdgen.py docs/            # process all .md files under docs/ recursively
    python mdgen.py file.md          # process a single file
"""

import csv
import re
import sys
from pathlib import Path
from typing import Callable


# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------

# Matches --key value  or  --flag (bare, no value).
# Flag values may be double-quoted, single-quoted, or bare words.
_FLAG_RE = re.compile(r'--(\w+)(?:\s+(?!--)(?:"([^"]*)"|\'([^\']*)\'|(\S+)))?')


def parse_tag_args(raw: str) -> tuple[str, dict[str, str]]:
    """Parse a tag's argument string into a positional arg and a kwargs dict.

    The positional argument may be quoted (double or single quotes) to support
    paths with spaces.  Keyword arguments use ``--key value`` or bare
    ``--flag`` (stored as ``{"flag": "true"}``).  Flag values may also be
    quoted.  Everything before the first ``--`` token is the positional.

    Examples
    --------
    >>> parse_tag_args("path/to/file.csv")
    ('path/to/file.csv', {})
    >>> parse_tag_args('"path with spaces/file.csv"')
    ('path with spaces/file.csv', {})
    >>> parse_tag_args("--reverse")
    ('', {'reverse': 'true'})
    >>> parse_tag_args("file.txt --reverse --key upper")
    ('file.txt', {'reverse': 'true', 'key': 'upper'})
    >>> parse_tag_args('"my docs/file.txt" --reverse')
    ('my docs/file.txt', {'reverse': 'true'})
    """
    raw = raw.strip()
    kwargs: dict[str, str] = {}

    # A leading quoted token is the positional argument.
    quoted = re.match(r'^(["\'])(.+?)\1\s*', raw)
    if quoted:
        positional = quoted.group(2)
        rest = raw[quoted.end():]
    else:
        flag_start = raw.find("--")
        if flag_start == -1:
            return raw, kwargs
        positional = raw[:flag_start].strip()
        rest = raw[flag_start:]

    for m in _FLAG_RE.finditer(rest):
        key = m.group(1)
        # groups 2/3/4: double-quoted / single-quoted / bare value
        value = (m.group(2) if m.group(2) is not None else
                 m.group(3) if m.group(3) is not None else
                 m.group(4) if m.group(4) is not None else
                 "true")
        kwargs[key] = value

    return positional, kwargs


def _bool_kwarg(kwargs: dict[str, str], key: str, default: bool = False) -> bool:
    """Return the boolean interpretation of a ``--flag`` / ``--key value`` kwarg."""
    val = kwargs.get(key, "").lower()
    if val in ("1", "true", "yes"):
        return True
    if val in ("0", "false", "no"):
        return False
    return default


# ---------------------------------------------------------------------------
# Generators
#
# Every generator has the signature:
#
#   fn(positional: str, old_content: str, **kwargs: str) -> str
#
# positional   — bare (pre-flag) part of the tag argument, stripped;
#                empty string when omitted.
# old_content  — text currently between the opening and closing tags,
#                stripped of surrounding newlines; use for in-place edits.
# **kwargs     — key/value pairs from --key value / --flag tokens.
# ---------------------------------------------------------------------------

def csv_to_markdown(positional: str, old_content: str, **kwargs: str) -> str:
    """Render a CSV file as a Markdown table.

    Required positional arg: path to the CSV file.
    """
    if not positional:
        raise ValueError("@csv requires a file path argument")

    path = Path(positional)
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {positional}")

    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    if not rows:
        return ""

    rows = [[cell.strip() for cell in row] for row in rows]
    headers = rows[0]
    data = rows[1:]
    n = len(headers)

    data = [(row + [""] * n)[:n] for row in data]
    bold_headers = [f"**{h}**" if h else "" for h in headers]

    col_widths = [len(bh) for bh in bold_headers]
    for row in data:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(cell))

    def fmt_row(cells: list[str]) -> str:
        parts = [cells[i].center(col_widths[i]) for i in range(n)]
        return "| " + " | ".join(parts) + " |"

    sep_parts = [":" + "-" * (col_widths[i] - 2) + ":" for i in range(n)]
    separator = "| " + " | ".join(sep_parts) + " |"

    lines = [fmt_row(bold_headers), separator] + [fmt_row(row) for row in data]
    return "\n".join(lines)


def sort_lines(positional: str, old_content: str, **kwargs: str) -> str:
    """Sort lines alphabetically.

    Without a positional argument the block's existing content is sorted
    in-place.  With a file path the file's lines are read and sorted.

    Keyword args
    ------------
    --reverse           Sort in descending order.
    --key upper|lower   Normalise each line before comparing (does not
                        change the output text, only the sort order).
    """
    reverse = _bool_kwarg(kwargs, "reverse")
    key_mode = kwargs.get("key", "").lower()

    if positional:
        path = Path(positional)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {positional}")
        with open(path, encoding="utf-8") as f:
            lines = [line.rstrip("\n\r") for line in f]
    else:
        lines = old_content.splitlines()

    def sort_key(line: str) -> str:
        if key_mode == "upper":
            return line.upper()
        if key_mode == "lower":
            return line.lower()
        return line

    return "\n".join(sorted(lines, key=sort_key, reverse=reverse))

def enumerate_list(positional: str, old_content: str, **kwargs: str) -> str:
    """Enumerate lines in a list, fixing any existing numbering.

    Strips leading list markers (``-``, ``*``, ``+``, or any existing
    ``N.``/``N)`` prefix) and re-numbers from 1.  Blank lines and lines
    that consist only of whitespace are preserved as-is (not numbered).

    Without a positional argument the block's existing content is
    re-enumerated in-place.  With a file path the file's lines are read
    and enumerated from scratch.

    Keyword args
    ------------
    --start N       Start numbering from N instead of 1.
    --keep_blanks   Include blank lines in the count (default: skip them).
    """
    start = int(kwargs.get("start", "1"))
    keep_blanks = _bool_kwarg(kwargs, "keep_blanks")

    if positional:
        path = Path(positional)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {positional}")
        with open(path, encoding="utf-8") as f:
            lines = [line.rstrip("\n\r") for line in f]
    else:
        lines = old_content.splitlines()

    # Strip any existing list marker: "- ", "* ", "+ ", "1. ", "2) ", etc.
    _MARKER_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)]) ?")

    output: list[str] = []
    counter = start
    for line in lines:
        if not line.strip():
            if keep_blanks:
                output.append(f"{counter}. ")
                counter += 1
            else:
                output.append("")
        else:
            clean = _MARKER_RE.sub("", line)
            output.append(f"{counter}. {clean}")
            counter += 1

    return "\n".join(output)
# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

# Opening tag forms (colon and argument are both optional):
#   <!-- @tag -->                     bare tag, no args
#   <!-- @tag: positional -->         colon + positional
#   <!-- @tag: positional --flag -->  colon + positional + flags
#   <!-- @tag --flag -->              flags only, no colon
#
# Group 3 captures the raw argument text (colon included when present);
# process_text strips the leading colon before passing to parse_tag_args.
_BLOCK_RE = re.compile(
    r"(<!-- @(\w+)((?::[^>]*?|(?:\s+--\w[^>]*?)))?\s*-->)"  # opening tag (groups 1-3)
    r"(.*?)"                                                  # existing content (group 4)
    r"(<!-- @end -->)",                                       # closing tag  (group 5)
    re.DOTALL,
)


class MarkdownProcessor:
    """Maps tag names to generator callables and processes markdown text/files.

    Generator signature::

        fn(positional: str, old_content: str, **kwargs: str) -> str

    Usage
    -----
    processor = MarkdownProcessor()
    processor.add("csv", csv_to_markdown)
    processor.add("sort_lines", sort_lines)
    processor.remove("csv")
    processor["csv"] = my_csv        # silent overwrite

    # Process a string directly:
    new_text, count = processor.process_text(text)

    # Process a file in-place (two equivalent forms):
    processor.process_file(Path("docs/index.md"))
    processor(Path("docs/index.md"))
    """

    def __init__(self) -> None:
        self._generators: dict[str, Callable[..., str]] = {}

    # ------------------------------------------------------------------
    # Generator management
    # ------------------------------------------------------------------

    def add(self, tag: str, fn: Callable[..., str]) -> None:
        """Register *fn* under *tag*.

        Raises ``ValueError`` if *tag* is already registered.  Use
        ``registry[tag] = fn`` to overwrite silently.
        """
        if tag in self._generators:
            raise ValueError(
                f"Tag '@{tag}' is already registered. "
                "Call remove() first, or assign via registry[tag] = fn."
            )
        self._generators[tag] = fn

    def remove(self, tag: str) -> None:
        """Unregister *tag*. Raises ``KeyError`` if not registered."""
        if tag not in self._generators:
            raise KeyError(f"Tag '@{tag}' is not registered.")
        del self._generators[tag]

    def __contains__(self, tag: str) -> bool:
        return tag in self._generators

    def __getitem__(self, tag: str) -> Callable[..., str]:
        return self._generators[tag]

    def __setitem__(self, tag: str, fn: Callable[..., str]) -> None:
        self._generators[tag] = fn

    def tags(self) -> list[str]:
        """Return a sorted list of registered tag names."""
        return sorted(self._generators)

    # ------------------------------------------------------------------
    # Processing
    # ------------------------------------------------------------------

    def process_text(self, text: str) -> tuple[str, int]:
        """Replace all generator blocks in *text*.

        Returns ``(new_text, block_count)`` where *block_count* is the number
        of blocks found (not necessarily changed).
        """
        errors: list[str] = []

        def replace(m: re.Match) -> str:
            open_tag, tag, raw_arg, old_content, close_tag = m.groups()
            raw_arg = (raw_arg or "").lstrip(":").strip()
            old_content = (old_content or "").strip("\n")

            if tag not in self:
                errors.append(f"Unknown tag '@{tag}'")
                return m.group(0)

            positional, kwargs = parse_tag_args(raw_arg)

            if positional and not Path(positional).is_absolute():
                positional = str(Path.cwd() / positional)

            try:
                generated = self[tag](positional, old_content, **kwargs)
            except Exception as e:
                errors.append(f"@{tag}: {e}")
                return m.group(0)

            return f"{open_tag}\n{generated}\n{close_tag}"

        new_text = _BLOCK_RE.sub(replace, text)
        count = len(_BLOCK_RE.findall(text))

        for err in errors:
            print(f"  [error] {err}", file=sys.stderr)

        return new_text, count

    def process_file(self, md_path: Path) -> None:
        """Process a single markdown file in-place."""
        text = md_path.read_text(encoding="utf-8")
        new_text, count = self.process_text(text)

        if count == 0:
            print("  (no generator blocks found)")
            return

        if new_text == text:
            print("  (no changes)")
            return

        md_path.write_text(new_text, encoding="utf-8")
        print(f"  updated {count} block(s)")

    def __call__(self, md_path: Path) -> None:
        """Alias for ``process_file``; allows ``registry(path)``."""
        self.process_file(md_path)


# Default registry used by main().
registry = MarkdownProcessor()
registry.add("csv", csv_to_markdown)
registry.add("sort_lines", sort_lines)
registry.add("enumerate_list", enumerate_list)

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    args = sys.argv[1:]

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
        registry(md_file)


if __name__ == "__main__":
    main()
