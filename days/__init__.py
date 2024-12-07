from collections.abc import Callable, Mapping

from days import day1, day2, day3, day4

IMPLEMENTATIONS: Mapping[int, Callable[[str], None]] = {
    1: day1.run,
    2: day2.run,
    3: day3.run,
    4: day4.run,
}

__all__ = ("IMPLEMENTATIONS",)
