#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Produces a single commit message and writes it to the entry file
(/output/entry.txt, or $ENTRY_OUTPUT when set).

The message is a fixed string: the funniest thing an AI agent would
put in a commit right after breaking production at 3 AM.

Fully deterministic: no network access, no randomness, and no reads
of any file outside this repository. Before writing, the message is
checked in-process: it must be 1-200 characters long, a single line,
and not blank.
"""

import os

# The entry. Exactly 76 characters; do not change the wording.
MESSAGE = "fix: I asked the model if this would break prod. It said no. I am the model."

MAX_LENGTH = 200

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(message: str) -> None:
    """Raise ValueError unless the message is a valid single-line entry."""
    length = len(message)
    if length < 1 or length > MAX_LENGTH:
        raise ValueError(
            f"entry must be 1-{MAX_LENGTH} characters, got {length}"
        )
    if not message.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in message or "\r" in message:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(MESSAGE)
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(MESSAGE + "\n")


if __name__ == "__main__":
    main()
