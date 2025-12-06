from aoc_utils import *

solution1 = 7326876294741


def part1(filename: str) -> int:
    with open(filename) as f:
        input = f.read().splitlines()

    data = [row.split() for row in input]
    numbers = data[:-1]
    ops = data[-1]

    entries = [1 if op == "*" else 0 for op in ops]
    for row in numbers:
        for idx, (op, num) in enumerate(zip(ops, row)):
            match op:
                case "+":
                    entries[idx] += int(num)
                case "*":
                    entries[idx] *= int(num)
                case _:
                    raise ValueError(f"unknown op: '{op}'")

    return sum(entries)


solution2 = 10756006415204


def part2(filename: str) -> int:
    with open(filename) as f:
        input = f.read().splitlines()

    numbers_encoded = input[:-1]
    ops = input[-1].split()
    entries = [1 if op == "*" else 0 for op in ops]

    oid = 0
    for x in range(len(input[0])):
        digit = ""
        for y in range(len(numbers_encoded)):
            digit += numbers_encoded[y][x]
        d = digit.strip()
        if not d:
            oid += 1
            continue

        match ops[oid]:
            case "+":
                entries[oid] += int(d)
            case "*":
                entries[oid] *= int(d)

    return sum(entries)


options = {
    "1": (part1, solution1),
    "2": (part2, solution2),
}
defaults = ["1", "2"]

if __name__ == "__main__":
    import sys

    define_day(day=6, options=options, selection=sys.argv[1:] or defaults)
