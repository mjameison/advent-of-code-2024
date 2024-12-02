from pathlib import Path

MIN_CHANGE = 1
MAX_CHANGE = 3


def is_report_valid(report: list[int], *, increasing: bool) -> tuple[bool, bool]:
    def is_valid_transition(last: int, new: int) -> bool:
        diff = new - last
        if not increasing:
            diff = -diff
        return MIN_CHANGE <= diff <= MAX_CHANGE

    valid_no_remove = [True, is_valid_transition(report[0], report[1])]
    valid_with_remove = [True, True]
    for index in range(2, len(report)):
        base_valid = valid_no_remove[index - 1] and is_valid_transition(
            report[index - 1], report[index]
        )
        valid = (
            valid_with_remove[index - 1]
            and is_valid_transition(report[index - 1], report[index])
        ) or (
            valid_no_remove[index - 2]
            and is_valid_transition(report[index - 2], report[index])
        )
        valid_no_remove.append(base_valid)
        valid_with_remove.append(valid)

    return valid_no_remove[-1], valid_with_remove[-1] or valid_no_remove[-2]


def run(path: str) -> None:
    safe_line_count = 0
    fudged_line_count = 0
    bf_count = 0

    with Path(path).open() as file:
        for line in file:
            numbers = [int(x) for x in line.split()]

            p1i, p2i = is_report_valid(numbers, increasing=True)
            p1d, p2d = is_report_valid(numbers, increasing=False)

            safe_line_count += p1i or p1d
            fudged_line_count += p2i or p2d

    print(f"Part 1: {safe_line_count}")
    print(f"Part 2: {fudged_line_count}")
    print(f"Part 2: {bf_count}")
