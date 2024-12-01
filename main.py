import typer

import days.day1

IMPLEMENTATIONS = {1: days.day1.run}


def main(day: int, path: str | None = None) -> None:
    impl = IMPLEMENTATIONS.get(day)
    if impl is None:
        print(f"Implementation for day {day} not found.")
        return

    if path is None:
        path = f"inputs/{day}.txt"

    impl(path)


if __name__ == "__main__":
    typer.run(main)
