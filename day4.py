from aoc_utils import *

solution1 = 1578


def part1(filename: str) -> int:
    with open(filename) as f:
        rows = f.read().splitlines()

    result = 0

    for rowid, row in enumerate(rows):
        for cellid, cell in enumerate(row):
            if cell == "@":
                adjacent = 0
                for i in range(max(rowid - 1, 0), min(rowid + 2, len(rows))):
                    for j in range(max(cellid - 1, 0), min(cellid + 2, len(row))):
                        adjacent += 1 if rows[i][j] == "@" else 0
                if adjacent <= 4:
                    result += 1

    return result


solution2 = 10132


def part2(filename: str) -> int:
    with open(filename) as f:
        input = f.read().splitlines()

    result = 0
    removable = None
    rows = [[1 if cell == "@" else 0 for cell in row] for row in input]

    while removable != 0:
        removable = 0

        for rowid, row in enumerate(rows):
            for cellid, cell in enumerate(row):
                if cell == 1:
                    adjacent = 0
                    for i in range(max(rowid - 1, 0), min(rowid + 2, len(rows))):
                        for j in range(max(cellid - 1, 0), min(cellid + 2, len(row))):
                            adjacent += rows[i][j]
                    if adjacent <= 4:
                        removable += 1
                        rows[rowid][cellid] = 0

        result += removable

    return result


def part2_visual(filename: str) -> int:
    from time import sleep

    with open(filename) as f:
        rows = f.read().splitlines()

    result = 0
    removable = None

    while removable != 0:
        removable = 0
        print("\n".join(rows))
        sleep(0.1)

        printy = ""
        for rowid, row in enumerate(rows):
            printy += "\n"
            newrow = ""
            for cellid, cell in enumerate(row):
                if cell == "@":
                    adjacent = 0
                    for i in range(max(rowid - 1, 0), min(rowid + 2, len(rows))):
                        for j in range(max(cellid - 1, 0), min(cellid + 2, len(row))):
                            adjacent += 1 if rows[i][j] == "@" else 0
                    if adjacent <= 4:
                        removable += 1
                    if adjacent <= 4:
                        newrow += "."
                        printy += "X"
                    else:
                        newrow += "@"
                        printy += "@"
                else:
                    newrow += "."
                    printy += "."

            rows[rowid] = newrow

        result += removable

        print(printy)
        sleep(0.1)

    return result


options = {
    "1": (part1, solution1),
    "2": (part2, solution2),
    "2v": (part2_visual, solution2),
}
defaults = ["1", "2"]

if __name__ == "__main__":
    import sys

    define_day(day=4, options=options, selection=sys.argv[1:] or defaults)
