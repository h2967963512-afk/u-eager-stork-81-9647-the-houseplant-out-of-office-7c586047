"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one out-of-office auto-reply, 116 characters,
# inside the 120-character gate: a houseplant abandoned since March
# whose water left with its owner, deflecting urgent mail to the
# cactus, who thrives on neglect.
# Revision note (parent pass): re-checked after the local run —
# the 116-character line is unchanged; this note only records the check.
import os

TEXT = (
    "Out of office. My owner left in March, and my water went "
    "with him. Urgent? Email the cactus — he thrives on neglect."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
