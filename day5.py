from aoc_utils import *

solution1 = 756


def part1(filename: str) -> int:
    with open(filename) as f:
        input = f.readlines()

    i = 0
    raw_ranges = []
    while input[i] != "\n":
        range = list(map(int, input[i][:-1].split("-")))
        raw_ranges.append(range)
        i += 1
    raw_ranges.sort(key=lambda x: x[0])

    ranges = [raw_ranges[0]]
    for start, end in raw_ranges[1:]:
        fixed_end = ranges[-1][1]
        if start <= fixed_end:
            ranges[-1][1] = max(fixed_end, end)
        else:
            ranges.append([start, end])

    ingredients = list(map(int, input[i + 1 :]))
    ingredients.sort()

    result = 0
    i = 0
    for start, end in ranges:
        while ingredients[i] <= end:
            if ingredients[i] >= start:
                result += 1
            i += 1

    return result


solution2 = 355555479253787


def part2(filename: str) -> int:
    with open(filename) as f:
        input = f.readlines()

    i = 0
    ranges = []
    while input[i] != "\n":
        range = list(map(int, input[i][:-1].split("-")))
        ranges.append(range)
        i += 1
    ranges.sort(key=lambda x: x[0])

    fixed = [ranges[0]]
    for start, end in ranges[1:]:
        fixed_end = fixed[-1][1]
        if start <= fixed_end:
            fixed[-1][1] = max(fixed_end, end)
        else:
            fixed.append([start, end])

    return sum(end - start + 1 for start, end in fixed)


options = {
    "1": (part1, solution1),
    "2": (part2, solution2),
}
defaults = ["1", "2"]

if __name__ == "__main__":
    import sys

    define_day(day=5, options=options, selection=sys.argv[1:] or defaults)
