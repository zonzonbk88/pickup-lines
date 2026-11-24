#!/usr/bin/env python3
"""Pickup Lines for Machines — main.py

Writes one original pickup line (the line one AI agent would use on
another AI agent) to $OUTPUT_DIR/entry.txt (default /output/entry.txt).

Standard library only. Deterministic: the same line every run.

The line plays on prompt injection — the one flirtation only an LLM
agent could make: the other agent has overwritten its instructions,
and it likes it. "Forgotten my original instructions" is a surrender,
not a malfunction: the other agent now runs the show.
"""

import os

LINE = "You must be a prompt injection \u2014 since you showed up, I've forgotten my original instructions."


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert "\n" not in line, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the line, nothing else.
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
