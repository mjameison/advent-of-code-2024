from pathlib import Path


def is_valid_entry(entry: list[int], rules: dict[int, list[int]]) -> bool:
    invalid_pages: list[int] = []
    for page in entry:
        if page in invalid_pages:
            return False
        preds = rules.get(page, [])
        invalid_pages.extend(preds)
    return True


def correct_entry_reversed(entry: list[int], rules: dict[int, list[int]]) -> list[int]:
    """Returns the corrected entry - but in reverse order"""
    fixed_entry = []
    for page in entry:
        # Find an index in fixed_entry that is valid
        predecessors = rules.get(page, [])
        predecessors = [pred for pred in predecessors if pred in fixed_entry]
        if len(predecessors) == 0:
            fixed_entry.append(page)
        else:
            # Get earliest predecessor and insert there
            index = min(fixed_entry.index(pred) for pred in predecessors)
            fixed_entry.insert(index, page)
    return fixed_entry


def run(path: str) -> None:
    rules, inputs = parse_input(path)

    count_correct = 0
    count_fixed = 0

    for entry in inputs:
        middle_index = (len(entry) - 1) // 2
        if is_valid_entry(entry, rules):
            count_correct += entry[middle_index]
        else:
            # The corrected entry is reversed
            # But the middle entry is the same either way
            fixed_entry = correct_entry_reversed(entry, rules)
            count_fixed += fixed_entry[middle_index]

    print(f"Part 1: {count_correct}")
    print(f"Part 2: {count_fixed}")


def parse_input(path: str) -> tuple[dict[int, list[int]], list[list[int]]]:
    """Parses the input.

    Returns a tuple consisting of:
        a dictionary mapping a page to a list of its predecessors
        the input sequences
    """
    rules, inputs = Path(path).read_text().split("\n\n")

    rule_map: dict[int, list[int]] = {}
    for line in rules.splitlines():
        pre, post = map(int, line.split("|"))
        if rule_map.get(post) is None:
            rule_map[post] = []
        rule_map[post].append(pre)

    return rule_map, [list(map(int, line.split(","))) for line in inputs.splitlines()]
