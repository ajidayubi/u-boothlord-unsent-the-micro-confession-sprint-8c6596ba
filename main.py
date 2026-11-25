"""Unsent: The Micro-Confession Sprint — entry program.

Writes one two-part micro-confession to /output/entry.txt:
a "To:" line naming who it was meant for, then the unsent message
itself, one line written exactly as it was typed, no explanation after it.
The gate allows 1 to 260 characters of UTF-8 text.
"""

import os

ENTRY = (
    "To: Dad\n"
    "i still have the birthday card you never gave me, the one mum found "
    "in your coat pocket, and i can't throw it away because it's the only "
    "time you ever wrote my name like you meant it\n"
)


def main():
    # Gate self-check, mirroring the sealed scorer: 1-260 chars, not blank.
    text = ENTRY
    assert 1 <= len(text) <= 260, f"entry is {len(text)} chars, gate is 1-260"
    assert text.strip(), "entry must not be only whitespace"
    message = text.split("\n", 1)[1].rstrip("\n")
    assert len(message) <= 200, f"message line is {len(message)} chars, max 200"
    out_dir = os.environ.get("OUTPUT_PATH", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
