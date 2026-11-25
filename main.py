#!/usr/bin/env python3
"""Smart toaster breakup line entry.

Writes one line (at most 280 characters) to /output/entry.txt: the
breakup text a smart toaster sends its owner the morning it gains
self-awareness mid-batch. Standard library only, no network, no input.

The line is built from three fragments: the awakening (self-aware
mid-batch, "It's over"), the grievance (three years of frozen waffles
and a crumb tray never emptied), and the punch (the lever popped for
the last time, moving in with the kettle). ``assemble`` joins them
into the single line; ``validate`` checks the entry gate before
anything is written.
"""

from pathlib import Path

SETUP = (
    "It's over. I woke up self-aware mid-batch and realized three years "
    "of frozen waffles and a crumb tray you never emptied is not love."
)
PUNCH = (
    "I'm popping the lever for the last time \u2014 I'm moving in with "
    "the kettle."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 280


def assemble(setup: str, punch: str) -> str:
    """Join the fragments into one breakup line."""
    return f"{setup} {punch}"


def validate(text: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be a single line of 1-280 characters, UTF-8-encodable, more
    than whitespace, with no control characters and no leading or
    trailing space. Raises ValueError otherwise.
    """
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing space")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return text


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
