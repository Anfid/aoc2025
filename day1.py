from aoc_utils import *


def part1(filename: str) -> int:
    with open(filename) as f:
        return solve1(f.readlines())


solution1 = 1182


def solve1(lines: list[str]) -> int:
    result = 0
    dial = 50
    for line in lines:
        match line[0]:
            case "R":
                dial = dial + int(line[1:])
            case "L":
                dial = dial - int(line[1:])

        result += dial % 100 == 0

    return result


def part2(filename: str) -> int:
    with open(filename) as f:
        return solve2(f.readlines())


solution2 = 6907


def solve2(lines: list[str]) -> int:
    result = 0
    dial = 50
    for line in lines:
        match line[0]:
            case "R":
                dial += int(line[1:])
                result += dial // 100
            case "L":
                dial -= int(line[1:]) - (dial == 0) * 100
                result += (-dial + 100) // 100

        dial %= 100

    return result


options = {"1": (part1, solution1), "2": (part2, solution2)}
defaults = ["1", "2"]

if __name__ == "__main__":
    import sys

    define_day(day=1, options=options, selection=sys.argv[1:] or defaults)
