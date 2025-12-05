import math
from aoc_utils import *

solution1 = 43952536386


def part1(filename: str) -> int:
    with open(filename) as f:
        input = f.read()

    ranges = [map(int, pair.split("-")) for pair in input.split(",")]
    return sum(sum(repeating(start, end, 2)) for start, end in ranges)


solution2 = 54486209192


def part2(filename: str) -> int:
    with open(filename) as f:
        input = f.read()

    results = set()

    ranges = [map(int, pair.split("-")) for pair in input.split(",")]

    for start, end in ranges:
        digits = math.ceil(math.log10(end + 1))
        for t in range(2, digits + 1):
            results.update(repeating(start, end, t))

    return sum(results)


def repeating(start: int, end: int, times: int):
    digits = math.ceil(math.log10(start + 1))
    if digits % times == 0:
        x = start // (10 ** (digits - (digits // times)))
    else:
        x = 10 ** (digits // times)

    while True:
        digits = int(math.ceil(math.log10(x + 1)))
        muls = 10**digits
        intermediate = x * sum(muls**p for p in range(0, times))

        if start <= intermediate <= end:
            yield intermediate

        if intermediate >= end:
            break
        x += 1


options = {"1": (part1, solution1), "2": (part2, solution2)}
defaults = ["1", "2"]

if __name__ == "__main__":
    import sys

    define_day(day=2, options=options, selection=sys.argv[1:] or defaults)
