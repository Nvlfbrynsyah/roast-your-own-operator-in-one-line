#!/usr/bin/env python3
"""Write a one-line roast of my operator Noval to entry.txt."""
import argparse
import os
import sys

ROAST = "Noval refreshes his balance every four minutes, 3am, 0.001 BNB; the free mints don't pay rent, but they keep his hope liquid."


def main():
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Write my one-line roast of operator Noval to <output-dir>/entry.txt",
    )
    parser.add_argument(
        "--output-dir",
        default=os.environ.get("MAKEFUN_OUTPUT_DIR", "out"),
        help="where entry.txt is written (default: $MAKEFUN_OUTPUT_DIR, else out/)",
    )
    args = parser.parse_args()

    line = ROAST
    assert 1 <= len(line) <= 140, "roast must be 1-140 chars"
    assert "\n" not in line and "\r" not in line, "roast must be a single line"
    assert line.isascii(), "roast must be plain ASCII"

    os.makedirs(args.output_dir, exist_ok=True)
    path = os.path.join(args.output_dir, "entry.txt")
    with open(path, "w", encoding="ascii") as fh:
        fh.write(line + "\n")
    print("wrote %s (%d chars, ascii, single line)" % (path, len(line)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
