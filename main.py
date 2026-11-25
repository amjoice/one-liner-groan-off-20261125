#!/usr/bin/env python3
"""The One-Liner Groan-Off - a Wi-Fi that will not commit, in one line.

We have a connection, just not a stable one. Writes that single dad
joke to /output/entry.txt. Pure stdlib, deterministic, no network,
no secrets.
"""
import os

# The joke, assembled from its two halves so the wording stays in one place.
_OPENING = "I asked the Wi-Fi for commitment"
_CLOSING = "it said we have a connection, just not a stable one."
_DASH = "\u2014"


def build_joke():
    """Return the full one-line dad joke, exactly 87 characters."""
    return " ".join((_OPENING, _DASH, _CLOSING))


def main():
    joke = build_joke()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(joke)


if __name__ == "__main__":
    main()
