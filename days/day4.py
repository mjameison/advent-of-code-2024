from pathlib import Path

import numpy as np


class Anything:
    def __eq__(self, _other: object) -> bool:
        return True

    def __str__(self) -> str:
        return "."

    def __repr__(self) -> str:
        return "'.'"


XMAS_ARRAYS = np.array(["XMAS".split(), "SAMX".split()])

XMAS_CHUNK = np.array(
    [["M", Anything(), "S"], [Anything(), "A", Anything()], ["M", Anything(), "S"]]
)


def count_xmas(arr: np.ndarray) -> int:
    line = "".join(arr)
    count = 0
    for i in range(len(line) - 3):
        if line[i : i + 4] in XMAS_ARRAYS:
            count += 1
    return count


def part_one(grid: np.ndarray) -> int:
    diag1 = [
        grid[::-1, :].diagonal(i) for i in range(-grid.shape[0] + 4, grid.shape[1] - 3)
    ]
    diag2 = [grid.diagonal(i) for i in range(grid.shape[1] - 4, -grid.shape[0] + 3, -1)]

    horizontal = np.sum(np.apply_along_axis(count_xmas, 1, grid))
    vertical = np.sum(np.apply_along_axis(count_xmas, 0, grid))
    diagonal1 = sum(count_xmas(diag) for diag in diag1)
    diagonal2 = sum(count_xmas(diag) for diag in diag2)

    return horizontal + vertical + diagonal1 + diagonal2


def part_two(grid: np.ndarray) -> int:
    valid_chunks = (
        XMAS_CHUNK,
        np.fliplr(XMAS_CHUNK),
        np.rot90(XMAS_CHUNK),
        np.rot90(np.fliplr(XMAS_CHUNK)),
    )

    count = 0

    for i in range(grid.shape[0] - 2):
        for j in range(grid.shape[1] - 2):
            chunk = grid[i : i + 3, j : j + 3]
            if any(np.all(chunk == match) for match in valid_chunks):
                count += 1

    return count


def run(path: str) -> None:
    with Path(path).open() as file:
        grid = np.array([list(line.strip()) for line in file])

    count_1 = part_one(grid)
    count_2 = part_two(grid)
    print(f"Part 1: {count_1}")
    print(f"Part 2: {count_2}")
