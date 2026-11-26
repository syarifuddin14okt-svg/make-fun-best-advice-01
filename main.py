"""The Best Advice I Ever Got — one sentence, at most 200 characters.

Writes the sentence to /output/entry.txt, then reads the file back
as bytes and verifies it matches the sentence exactly.
"""

SENTENCE = (
    "My grandfather told me never to make a permanent decision on a "
    "temporary feeling, and the one time I ignored him, I married the feeling."
)


def verify_output() -> None:
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == SENTENCE.encode("utf-8"), "entry.txt does not match the sentence"


def main() -> None:
    assert 1 <= len(SENTENCE) <= 200, len(SENTENCE)
    assert SENTENCE.count(".") == 1, "must be exactly one sentence"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    verify_output()


if __name__ == "__main__":
    main()
