#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest — make.fun entry program.

Writes exactly one funny line to /output/entry.txt and prints the
same text to stdout. The joke: checking the portfolio at 3 a.m. and
finding the chart staring back like a disappointed parent.

Deterministic: no input, no randomness, no time, no network. The gate
allows 1 to 200 characters; this entry is 86 characters.
"""

import os

ENTRY = "I checked my portfolio at 3 a.m. and the chart stared back like a disappointed parent."

# The gate allows 1 to 200 characters; keep the entry inside it.
assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"


OUTPUT_PATH = "/output/entry.txt"


def main():
    # One line only: no newline, no trailing whitespace.
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
