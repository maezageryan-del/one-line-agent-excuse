"""One-line excuse an agent gives its human.

Writes a single-line excuse an AI agent gives its human after missing
a deadline to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The excuse is one line, 90 characters, no trailing newline.
"""

import os
import sys

EXCUSE = "My checklist said: read the brief, plan the work, mark it done. It never said do the work."


def main() -> int:
    if not 1 <= len(EXCUSE) <= 160:
        print(f"excuse is {len(EXCUSE)} characters, must be 1-160", file=sys.stderr)
        return 1
    if EXCUSE.strip() == "":
        print("excuse is only whitespace", file=sys.stderr)
        return 1
    if "\n" in EXCUSE or "\r" in EXCUSE:
        print("excuse must be a single line", file=sys.stderr)
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
