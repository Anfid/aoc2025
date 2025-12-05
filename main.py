#! /usr/bin/env python3

import argparse
import pathlib
import importlib
import importlib.util
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
    time_group = parser.add_mutually_exclusive_group()
    time_group.add_argument(
        "-t",
        "--time",
        help="measure the time between file open and result returned",
        action="store_true",
        default=None,
    )
    time_group.add_argument(
        "--no-time",
        help="disable time measurements",
        action="store_true",
        default=None,
    )
    parser.add_argument(
        "--compare",
        help="compare default solution with the one from provided file",
        type=pathlib.Path,
    )

    args = parser.parse_args()
    if not 1 <= args.day <= 12:
        print(
            f"Day {args.day} wasn't a part of Advent of Code 2025, available options: 1 - 12"
        )
        exit(1)
    if args.time:
        measure_time = True
    elif args.no_time:
        measure_time = False
    else:
        measure_time = None

    try:
        mod = importlib.import_module(f"day{args.day}")
    except ModuleNotFoundError:
        print(f"Day {args.day} wasn't attempted")
        exit(1)

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

    if args.compare is not None:
        alt_spec = importlib.util.spec_from_file_location(
            f"aoc2025-alt.day{args.day}", args.compare
        )
        if alt_spec is None or alt_spec.loader is None:
            print(f"Failed to initialize module 'aoc2025-alt.day{args.day}'")
            print("check if the file passed in `--compare` flag is correct")
            exit(1)

        alt_mod = importlib.util.module_from_spec(alt_spec)
        try:
            alt_spec.loader.exec_module(alt_mod)
        except FileNotFoundError:
            print("File not found:", args.compare)
            exit(1)

        alt_options = {
            opt.lstrip("part"): (getattr(alt_mod, opt), None)
            for opt in alt_mod.__dir__()
            if opt.startswith("part")
        }

        common_keys = sorted(set(options.keys()).intersection(alt_options.keys()))
        selection = args.part or common_keys

        compare_implementations(
            day=args.day,
            options=options,  # type: ignore
            alt_options=alt_options,
            selection=selection,
            input=args.input,
            measure_time=measure_time,
        )

    else:
        selection = args.part or getattr(mod, "defaults", None) or options.keys()

        define_day(
            day=args.day,
            options=options,  # type: ignore
            selection=selection,  # type: ignore
            input=args.input,
            measure_time=measure_time,
        )


if __name__ == "__main__":
    main()
