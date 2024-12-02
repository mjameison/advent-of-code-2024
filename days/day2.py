from pathlib import Path

MIN_CHANGE = 1
MAX_CHANGE = 3


def is_report_valid(report: list[int], *, increasing: bool) -> tuple[bool, bool]:
    def is_valid_transition(last: int, new: int) -> bool:
        diff = new - last
        if not increasing:
            diff = -diff
        return MIN_CHANGE <= diff <= MAX_CHANGE

    # a_x is all included to x back is valid
    a_2, a_1 = True, is_valid_transition(report[0], report[1])
    # s_x is all included with 1 skip to x back is valid
    s_1 = True

    for index in range(2, len(report)):
        # t_x is if the transition from x back to current valid
        t_1 = is_valid_transition(report[index - 1], report[index])
        t_2 = is_valid_transition(report[index - 2], report[index])
        a_0 = a_1 and t_1
        s_0 = (s_1 and t_1) or (a_2 and t_2)

        a_2, a_1 = a_1, a_0
        s_1 = s_0

    return a_1, s_1 or a_2


def run(path: str) -> None:
    safe_line_count = 0
    fudged_line_count = 0

    with Path(path).open() as file:
        for line in file:
            numbers = [int(x) for x in line.split()]

            p1i, p2i = is_report_valid(numbers, increasing=True)
            p1d, p2d = is_report_valid(numbers, increasing=False)

            safe_line_count += p1i or p1d
            fudged_line_count += p2i or p2d

    print(f"Part 1: {safe_line_count}")
    print(f"Part 2: {fudged_line_count}")
