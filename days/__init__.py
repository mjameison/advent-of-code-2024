from collections.abc import Callable, Mapping

from days import day1, day2, day3

IMPLEMENTATIONS: Mapping[int, Callable[[str], None]] = {
    1: day1.run,
    2: day2.run,
    3: day3.run,
}

__all__ = ("IMPLEMENTATIONS",)
