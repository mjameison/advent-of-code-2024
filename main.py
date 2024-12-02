import typer

import days


def main(day: int, path: str | None = None) -> None:
    impl = days.IMPLEMENTATIONS.get(day)
    if impl is None:
        print(f"Implementation for day {day} not found.")
        return

    if path is None:
        path = f"inputs/{day}.txt"

    impl(path)


if __name__ == "__main__":
    typer.run(main)
