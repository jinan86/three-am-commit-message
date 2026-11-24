#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Writes one commit message to /output/entry.txt: the funniest thing an AI
agent would put in a commit right after breaking production at 3 AM.

Deterministic: no network, no randomness, no files read outside this repo.
The message is a fixed constant, validated in-process to be 1-200 UTF-8
characters, a single line, and not only whitespace.
"""

import os

ENTRY = "fix: I asked the model if this would break prod. It said no. I am the model."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    message = ENTRY
    if not message or not message.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in message or "\r" in message:
        raise ValueError("entry must be a single line")
    if not 1 <= len(message) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(message)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(message + "\n")


if __name__ == "__main__":
    main()
