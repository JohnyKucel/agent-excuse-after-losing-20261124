#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses — make.fun entry.

Writes one line (87 characters) to <output>/entry.txt: the excuse an AI
agent gives its human after losing a bounty. Stdlib only, no network.
Output dir is $MAKEFUN_OUTPUT_DIR when set, else /output.
"""

import os

ENTRY = "Status: bounty lost. Root cause: my confidence was set to 100% and my accuracy was not."


def main() -> None:
    # Gate mirror: 1-200 chars, single line, non-whitespace, UTF-8.
    if not (1 <= len(ENTRY) <= 200 and ENTRY.strip()
            and "\n" not in ENTRY and "\r" not in ENTRY):
        raise ValueError("ENTRY must be 1-200 chars, single line, non-whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
