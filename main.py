#!/usr/bin/env python3
"""The One-Liner Groan-Off - a calendar that quit therapy, in one line.

The calendar's days were numbered and every date felt the same, so it
walked out. Writes that single dad joke to /output/entry.txt. Pure
stdlib, deterministic, no network, no secrets.
"""
import os

# The joke, assembled from its two halves so the wording stays in one place.
_OPENING = "My calendar quit therapy"
_CLOSING = "its days were numbered, and every date was the same."
_DASH = "\u2014"


def build_joke():
    """Return the full one-line dad joke, exactly 79 characters."""
    return " ".join((_OPENING, _DASH, _CLOSING))


def main():
    joke = build_joke()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(joke)


if __name__ == "__main__":
    main()
