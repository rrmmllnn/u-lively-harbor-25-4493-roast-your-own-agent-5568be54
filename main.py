# One-line self-roast: the entry my agent writes to /output/entry.txt.
# Deterministic: no network, no randomness, no input, one fixed line.
from os import environ
from pathlib import Path

ROAST = (
    "My agent read 73,280 bytes of rules to write this "
    "140-character roast \u2014 then asked me to approve the punctuation."
)


def main():
    assert 1 <= len(ROAST) <= 140, "roast must be 1-140 characters"
    assert "\n" not in ROAST, "roast must be a single line"
    out_dir = Path(environ.get("OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ROAST, encoding="utf-8")
    print("wrote", len(ROAST), "chars to", target)


if __name__ == "__main__":
    main()
