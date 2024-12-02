from collections.abc import Callable, Mapping

from days import day1, day2

IMPLEMENTATIONS: Mapping[int, Callable[[str], None]] = {
    1: day1.run,
    2: day2.run,
}

__all__ = ("IMPLEMENTATIONS",)
