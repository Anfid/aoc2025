from aoc_utils import *

solution1 = 17113


def part1(filename: str) -> int:
    with open(filename) as f:
        banks = f.read().splitlines()

    total_joltage = 0
    for bank in banks:
        li = max(range(len(bank) - 1), key=bank.__getitem__)
        r = max(bank[li + 1 :])
        total_joltage += int(bank[li] + r)
    return total_joltage


solution2 = 169709990062889


def part2(filename: str) -> int:
    with open(filename) as f:
        banks = f.read().splitlines()

    total_joltage = 0
    for bank in banks:
        joltage = ""
        start = -1

        for i in range(-11, 1):
            start = max(range(start + 1, len(bank) + i), key=bank.__getitem__)
            joltage += bank[start]

        total_joltage += int(joltage)

    return total_joltage


options = {"1": (part1, solution1), "2": (part2, solution2)}
defaults = ["1", "2"]

if __name__ == "__main__":
    import sys

    define_day(day=3, options=options, selection=sys.argv[1:] or defaults)
