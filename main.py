#!/usr/bin/env python3
"""Texts From Your Future Self — make.fun bounty entry.

Writes one funny text message from the writer's future self to
/output/entry.txt. Pure Python standard library, deterministic: the same
text every run, no network, no randomness, no environment input.
"""

import os

ENTRY = (
    "It's me, you, from 2046. Good news: you finally stop apologizing to "
    "the microwave. Bad news: you start apologizing to the fridge instead. "
    "Growth is weird."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.isprintable():
        raise ValueError("entry must contain only printable characters")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    try:
        os.chmod(OUTPUT_PATH, 0o644)
    except OSError:
        pass
    # Read back what was written and confirm it matches the entry exactly.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read().strip()
    if written != text:
        raise ValueError("written entry does not match the intended text")


if __name__ == "__main__":
    main()
