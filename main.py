#!/usr/bin/env python3
"""Write one original funny out-of-office auto-reply to entry.txt.

The line is a single out-of-office reply, one line long, written for
make.fun's "Funniest One-Line Out-of-Office Reply" bounty. It must be
1-160 characters of UTF-8 text, so we assert that before writing.
"""
import os
import sys

LINE = (
    "Out of office: my cat is watching my inbox. She has already replied "
    "to your email by walking across the keyboard, and whatever she said, "
    "it stands."
)


def main() -> int:
    if not (1 <= len(LINE) <= 160):
        print(f"line is {len(LINE)} chars, must be 1-160", file=sys.stderr)
        return 1
    if "\n" in LINE.strip():
        print("line must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
