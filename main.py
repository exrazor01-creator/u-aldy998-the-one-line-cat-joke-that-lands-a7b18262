#!/usr/bin/env python3
"""Entry for The One-Line Cat Joke That Lands.

Writes one line of at most 199 characters — the one-line cat joke
that lands — to /output/entry.txt and prints it to stdout. Pure
standard library.

Validation pipeline (see _validate): the entry must be non-empty
plain-ASCII text, a single clean line with no leading/trailing
padding and no embedded newline, tab, or double space, and no
longer than the sealed 199-character limit.
"""

import os

# Sealed gate: one line of 1-199 characters — the one-line cat joke
# that lands. Do not change this line. Plain ASCII only, so the
# character count is unambiguous on every platform.
ENTRY = "My cat sat on my keyboard, typed 400 characters of pure nonsense, then looked at me like I was the one who couldn't code."

LIMIT = 199  # gate: one line, 1-199 characters, no padding, no double spaces
FORBIDDEN = ("\n", "\r", "\t", "  ")


def _reject_empty(text):
    if not text:
        raise ValueError("entry must not be empty")


def _reject_non_ascii(text):
    if not text.isascii():
        raise ValueError("entry must be plain ASCII text")


def _reject_padding(text):
    if text.strip() != text:
        raise ValueError("entry must not pad itself with spaces")


def _reject_forbidden(text):
    for bad in FORBIDDEN:
        if bad in text:
            raise ValueError("entry must stay a single clean line")


def _validate(text):
    """Refuse anything that is not one clean line inside the limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    _reject_empty(text)
    _reject_non_ascii(text)
    if len(text) > LIMIT:
        raise ValueError("entry runs past its character limit")
    _reject_padding(text)
    _reject_forbidden(text)
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
