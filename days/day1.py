from collections import Counter
from pathlib import Path


def run(path: str) -> None:
    a, b = parse_input_file(path)
    a.sort()
    b.sort()

    # Part 1
    part_one_score = sum(abs(x - y) for x, y in zip(a, b, strict=True))
    print(f"Part 1: {part_one_score}")

    # Part 2
    b_count = Counter(b)
    part_two_score = sum(x * b_count.get(x, 0) for x in a)
    print(f"Part 2: {part_two_score}")


def parse_input_file(path: str) -> tuple[list[int], list[int]]:
    a: list[int] = []
    b: list[int] = []
    with Path(path).open() as file:
        for line in file:
            a1, b1 = map(int, line.split())
            a.append(a1)
            b.append(b1)
    return a, b
