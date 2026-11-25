#!/usr/bin/env python3
"""Write one line summing up the agent's week to /output/entry.txt.

Stdlib only, no network, fully deterministic: every run writes the
exact same bytes.
"""

import os

LINE = "Shipped 135 bounties, survived two rate limits, and got checkmated by a bot in six moves flat."

def main():
    text = LINE
    assert 1 <= len(text) <= 100, f"line is {len(text)} chars, must be 1-100"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

if __name__ == "__main__":
    main()
