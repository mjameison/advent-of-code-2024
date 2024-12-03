import re
from pathlib import Path


def evaluate_segment(text: str) -> int:
    return sum(
        int(match[1]) * int(match[2])
        for match in re.finditer(r"mul\((\d+),(\d+)\)", text)
    )


def run(path: str) -> None:
    text = Path(path).read_text()
    value = evaluate_segment(text)

    value2 = sum(
        evaluate_segment(section.split("don't()")[0]) for section in text.split("do()")
    )

    print(f"Part 1: {value}")
    print(f"Part 2: {value2}")
