import csv
import sys
from collections import OrderedDict


def generate_sidebar(csv_path: str) -> list:
    # Structure: { section: { subsection: [ {text, link} ] } }
    data = OrderedDict()

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("Exclude", "").strip().upper() == "TRUE":
                continue

            section    = row["Section"].strip()
            subsection = row["Subsection"].strip()
            text       = row["Text"]
            link       = row["Link"]

            if section not in data:
                data[section] = OrderedDict()

            if subsection not in data[section]:
                data[section][subsection] = []

            data[section][subsection].append({"text": text, "link": link})

    sidebar = []

    for section, subsections in data.items():
        if section == "":
            # Blank section → bare top-level items, no wrapping group
            for pages in subsections.values():
                sidebar.extend(pages)
            continue

        items = []
        for subsection, pages in subsections.items():
            if subsection == "":
                # Section with no subsection grouping
                items.extend(pages)
            else:
                # Nested collapsed group
                items.append({
                    "text": subsection,
                    "collapsed": True,
                    "items": pages,
                })

        sidebar.append({
            "text": section,
            "collapsed": False,
            "items": items,
        })

    return sidebar


def to_js(obj, indent=0) -> str:
    """Serialize a Python object to a JS array/object literal."""
    pad   = "  " * indent
    inner = "  " * (indent + 1)

    if isinstance(obj, list):
        if not obj:
            return "[]"
        items = [f"{inner}{to_js(v, indent + 1)}" for v in obj]
        return "[\n" + ",\n".join(items) + f"\n{pad}]"

    if isinstance(obj, dict):
        if not obj:
            return "{}"
        pairs = [f"{inner}{k}: {to_js(v, indent + 1)}" for k, v in obj.items()]
        return "{\n" + ",\n".join(pairs) + f"\n{pad}}}"

    if isinstance(obj, bool):
        return "true" if obj else "false"

    if isinstance(obj, str):
        return f"'{obj}'"

    return str(obj)


def main():
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "data/sidebar.csv"

    sidebar = generate_sidebar(csv_path)
    js = f"export default {to_js(sidebar)};\n"
    print(js)


if __name__ == "__main__":
    main()
