from time import perf_counter
from typing import Callable, Mapping


SolutionF = Callable[[str], int]


def define_day(
    day: int,
    options: Mapping[str, tuple[SolutionF, None | int]],
    selection: list[str],
    input: str | None = None,
):
    if input is None:
        input = f"./input/day{day}.txt"

    available_opts = options.keys()
    unknown_opts = [p for p in selection if p not in available_opts]
    if unknown_opts:
        print(
            f"Unknown option{'s' if len(unknown_opts) > 1 else ''}: {', '.join(unknown_opts)}"
        )
        print(
            f"Available option{'s' if len(available_opts) > 1 else ''}: {', '.join(available_opts)}"
        )
        exit(1)

    for i, part in enumerate(selection):
        f, s = options[part]

        if len(selection) > 1:
            print(f"Part {part}:")
        pretty_solver(f, input, s, set_clipboard=len(selection) == 1)
        if i < len(selection) - 1:
            print()


def try_copy(result: int):
    try:
        import pyperclip

        pyperclip.copy(str(result))
        print("Copied!")
    except:
        pass


def pretty_solver(
    fn: SolutionF,
    input: str,
    solution: int | None = None,
    measure_time: bool | None = None,
    set_clipboard: bool = True,
):
    start = perf_counter()
    res = fn(input)
    t = perf_counter() - start

    if solution is None:
        print(res)
        if set_clipboard:
            try_copy(res)
    elif isinstance(solution, SolutionHint):
        cmp = solution.compare(res)
        if cmp is True:
            print(res, "✔️")
            if set_clipboard:
                try_copy(res)
        elif cmp is False:
            print(res, "❌")
            print("This answer was explicitly marked as incorrect")
        elif cmp > 0:
            print(res, "❌")
            print(
                solution.greater_than,
                "was the previous undershoot, result must be MORE",
            )
        elif cmp < 0:
            print(res, "❌")
            print(
                solution.less_than,
                "was the previous overshoot, result must be LESS",
            )
        else:
            print("warning: Invalid hint check result")

    elif isinstance(solution, int):
        badge = "✅" if res == solution else "❌"
        print(res, badge)
        if res > solution:
            print(f"{solution} expected, result must be LESS")
        elif res < solution:
            print(f"{solution} expected, result must be MORE")
        if res != solution:
            print(f"diff: {abs(solution - res)}")
    else:
        print("warning: Invalid solution type")

    if (measure_time is None and res == solution) or measure_time is True:
        if t < 1:
            print(f"time: {t * 1000}ms")
        else:
            print(f"time: {t}s")


class SolutionHint:
    greater_than: int | None
    less_than: int | None
    incorrect: set[int]

    def __init__(
        self,
        greater_than: int | None = None,
        less_than: int | None = None,
        incorrect: set[int] = set(),
    ) -> None:
        if greater_than is not None and less_than is not None:
            assert (
                less_than - greater_than >= 1
            ), "Lower and upper bounds of solution hint intersect"
            assert less_than - greater_than != 2, f"Solution: {greater_than + 1}"
        self.greater_than = greater_than
        self.less_than = less_than
        self.incorrect = incorrect

    def compare(self, result: int) -> int | bool:
        if self.greater_than is not None and result <= self.greater_than:
            return self.greater_than - result
        if self.less_than is not None and result >= self.less_than:
            return self.less_than - result
        if result in self.incorrect:
            return False
        return True

    def __add__(self, other: SolutionHint) -> SolutionHint:
        gt = max(
            (v for v in (self.greater_than, other.greater_than) if v is not None),
            default=None,
        )
        lt = min(
            (v for v in (self.less_than, other.less_than) if v is not None),
            default=None,
        )
        incorrect = self.incorrect & other.incorrect
        return SolutionHint(greater_than=gt, less_than=lt, incorrect=incorrect)

    def __and__(self, value: SolutionHint) -> SolutionHint:
        return self + value


def over(base: int) -> SolutionHint:
    return SolutionHint(greater_than=base)


def under(base: int) -> SolutionHint:
    return SolutionHint(less_than=base)


def is_not(bad: int) -> SolutionHint:
    return SolutionHint(incorrect={bad})
