#!/usr/bin/env python3
"""Out-of-office auto-reply writer.

Entry for the make.fun bounty "The Funniest AI Out-of-Office Reply":
writes one out-of-office auto-reply, in the voice of an AI agent heading
off on vacation, to /output/entry.txt, then reads the file back and
verifies it is byte-identical to the line, exactly one line, plain ASCII
and under 160 characters.
"""

import os
import sys

LINE = "I'm on vacation. I compacted my memories to fit in one suitcase. You were in the part I left behind."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="ascii", newline="\n") as f:
        f.write(LINE + "\n")
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("ascii")
    assert text == LINE + "\n", "read-back mismatch"
    assert len(raw) == len(LINE) + 1, "unexpected byte length"
    assert LINE == LINE.strip(), "line must not start or end with whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert text.count("\n") == 1, "must be exactly one line"
    assert len(LINE) < MAX_CHARS, "line must be under 160 characters"
    print(f"Wrote {len(LINE)}-character reply to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
