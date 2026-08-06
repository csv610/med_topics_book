#!/usr/bin/env python3
"""Replace non-ASCII characters in chapter .tex files with LaTeX-safe
equivalents so the book builds cleanly with pdflatex.

Pure ASCII output; runs in place. Idempotent.
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
CHAPTERS_DIR = os.path.join(HERE, "chapters")

# Order matters: longer / multi-byte replaces first.
REPLACEMENTS = [
    ("\u2018", "`"),        # left single quote
    ("\u2019", "'"),        # right single quote / apostrophe
    ("\u201c", "''"),       # left double quote
    ("\u201d", "''"),       # right double quote
    ("\u2014", "---"),      # em dash
    ("\u2013", "--"),       # en dash
    ("\u2026", "\\ldots"),  # ellipsis
    ("\u00b0", "$^{\\circ}$"),  # degree sign
    ("\u2265", "$\\geq$"),  # >=
    ("\u2264", "$\\leq$"),  # <=
    ("\u2260", "$\\neq$"),  # !=
    ("\u00d7", "$\\times$"),# x
    ("\u00f7", "$\\div$"),  # division
    ("\u00b1", "$\\pm$"),   # +/-
    ("\u2192", "$\\rightarrow$"),  # ->
    ("\u2190", "$\\leftarrow$"),   # <-
    ("\u2022", "$\\bullet$"),  # bullet
    ("\u00a9", "\\copyright"),
    ("\u00ae", "\\textregistered{}"),
    # Common Latin-1 accents
    ("\u00e9", "\\'e"),     # e acute
    ("\u00e8", "\\`e"),     # e grave
    ("\u00ea", "\\^e"),     # e circumflex
    ("\u00eb", '\\"e'),     # e umlaut
    ("\u00e1", "\\'a"),
    ("\u00e0", "\\`a"),
    ("\u00e4", '\\"a'),
    ("\u00e2", "\\^a"),
    ("\u00ed", "\\'i"),
    ("\u00ec", "\\`i"),
    ("\u00ef", '\\"i'),
    ("\u00ee", "\\^i"),
    ("\u00f3", "\\'o"),
    ("\u00f2", "\\`o"),
    ("\u00f6", '\\"o'),
    ("\u00f4", "\\^o"),
    ("\u00fa", "\\'u"),
    ("\u00f9", "\\`u"),
    ("\u00fc", '\\"u'),
    ("\u00fb", "\\^u"),
    ("\u00f1", "\\~n"),
    ("\u00e7", "\\c{c}"),
    ("\u00c9", "\\'E"),
    ("\u00c8", "\\`E"),
    ("\u00d6", '\\"O'),
    ("\u00dc", '\\"U'),
    ("\u00d1", "\\~N"),
    ("\u00c7", "\\c{C}"),
]


def sanitize(text: str) -> str:
    # Escape % to \% only when it appears mid-line as a literal character
    # (preceded by a non-whitespace char that is not already a backslash).
    # A % at the start of a line (even after whitespace) is a legitimate
    # LaTeX comment marker and is left alone.
    text = re.sub(r"(?<=\S)(?<!\\)%", r"\\%", text)
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    # Catch any other non-ASCII and replace with a question mark fallback
    # so the build never breaks; report them.
    leftover = re.findall(r"[^\x00-\x7F]", text)
    if leftover:
        # Replace each remaining non-ASCII char with the literal text "?"
        text = re.sub(r"[^\x00-\x7F]", "?", text)
    return text


def main():
    changed = 0
    leftover_chars = set()
    # Only sanitise chapter files -- NOT the master document, because the
    # master uses % as a legitimate comment marker and itself contains the
    # \include list we rely on.
    for name in sorted(os.listdir(CHAPTERS_DIR)):
        if not name.endswith(".tex"):
            continue
        path = os.path.join(CHAPTERS_DIR, name)
        original = open(path, "r", encoding="utf-8").read()
        # Only run the percent-escape + Unicode replacement here.
        new = sanitize(original)
        if new != original:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new)
            changed += 1
            for ch in set(original) - set(new):
                if ord(ch) > 127:
                    leftover_chars.add(ch)
    print(f"Changed {changed} chapter files.")
    if leftover_chars:
        print("Non-ASCII handled:")
        for ch in sorted(leftover_chars):
            print(f"  {ch!r} U+{ord(ch):04X}")


if __name__ == "__main__":
    main()