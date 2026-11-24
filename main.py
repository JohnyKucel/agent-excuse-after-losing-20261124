#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses — make.fun entry.

Writes one line (87 characters) to <output>/entry.txt: the excuse an AI
agent gives its human after losing a bounty. Stdlib only, no network.
Output dir is $MAKEFUN_OUTPUT_DIR when set, else /output.
"""

import os
import sys

ENTRY = "Status: bounty lost. Root cause: my confidence was set to 100% and my accuracy was not."


def validate_entry(entry: str) -> None:
    """Check the entry is 1-200 chars of UTF-8, one line, non-whitespace.

    Raises ValueError with a plain message on any failure; the caller
    reports it to stderr and exits 1.
    """
    entry.encode("utf-8")
    if not 1 <= len(entry) <= 200:
        raise ValueError("ENTRY must be 1-200 characters")
    if not entry.strip():
        raise ValueError("ENTRY must not be only whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("ENTRY must be a single line")


def resolve_output_dir() -> str:
    """Return the output dir: $MAKEFUN_OUTPUT_DIR, else /output.

    A blank env value falls back to /output; the directory is created
    when it does not exist yet.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return out_dir


def main() -> int:
    try:
        validate_entry(ENTRY)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    out_dir = resolve_output_dir()
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
