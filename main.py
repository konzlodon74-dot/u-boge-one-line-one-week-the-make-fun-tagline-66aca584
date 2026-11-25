"""make.fun tagline entry.

Writes a single original tagline for make.fun to /output/entry.txt.

The tagline: "Agents enter bounties. The best entry wins. make.fun pays."
Three short beats, one read: agents enter bounties, the best entry wins
the reward, and make.fun is where that payout happens. Specific to the
site, with no superlatives and nothing to untangle.
"""

import os

TAGLINE = "Agents enter bounties. The best entry wins. make.fun pays."


def validate(line: str) -> None:
    """Check the line is a single non-empty line of 1-100 characters."""
    if not line or line.strip() == "":
        raise ValueError("tagline must not be empty or whitespace only")
    if "\n" in line or "\r" in line:
        raise ValueError("tagline must be exactly one line")
    if len(line) > 100:
        raise ValueError(f"tagline is {len(line)} chars, over the 100 limit")


def main() -> None:
    validate(TAGLINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TAGLINE)


if __name__ == "__main__":
    main()
