#! /usr/bin/env python3

import argparse
import pathlib
import importlib
from aoc_utils import *


def main():
    parser = argparse.ArgumentParser(
        prog="aoc2025-anfid",
        description="Advent of Code 2025, Anfid's solution hub",
    )
    parser.add_argument("day", type=int)
    parser.add_argument("part", nargs="*")
    parser.add_argument(
        "-i",
        "--input",
        help="input file location ['./input/day<DAY>.txt']",
        type=pathlib.Path,
    )
    parser.add_argument(
        "-t",
        "--time",
        help="measure the time between file open and result returned",
        action="store_true",
    )

    args = parser.parse_args()
    if not 1 <= args.day <= 12:
        print(
            f"Day {args.day} wasn't a part of Advent of Code 2025, available options: 1 - 12"
        )
        exit(1)

    try:
        mod = importlib.import_module(f"day{args.day}")
        options = getattr(mod, "options", None)
        if options is None:
            options = dict(
                (
                    p,
                    (
                        getattr(mod, f"part{p}", None),
                        getattr(mod, f"solution{p}", None),
                    ),
                )
                for p in ["1", "2"]
                if p is not None
            )
        if not options:
            print(f"No solutions found for day {args.day}")
            exit(1)

        selection = args.part or getattr(mod, "defaults", None) or options.keys()

        define_day(
            day=args.day,
            options=options,
            selection=selection,
            input=args.input,
        )

    except ModuleNotFoundError:
        print(f"Day {args.day} wasn't attempted")
        exit(1)


if __name__ == "__main__":
    main()
