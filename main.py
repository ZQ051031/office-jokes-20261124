"""One-line office joke entry for make.fun.

Writes a single original joke about office life to /output/entry.txt.
Standard library only, no network.

The entry must be UTF-8 text of 1 to 199 characters, not only whitespace,
per the sealed scorer's gate in the competition rules.
"""

import os

JOKE = "I replied-all to ask everyone to stop replying all, and now there's a company policy named after me."

MIN_CHARS = 1
MAX_CHARS = 199


def validate_entry(text):
    """Check the entry against the competition gate."""
    if not isinstance(text, str):
        raise TypeError("entry must be a str")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be %d to %d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(text))
        )
    text.encode("utf-8")  # must be valid UTF-8
    return text


def output_path():
    """Resolve the output file from the environment."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def write_entry(text, path):
    """Validate the joke and write it exactly, with no trailing junk."""
    entry = validate_entry(text)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    return path


def main():
    write_entry(JOKE, output_path())


if __name__ == "__main__":
    main()
