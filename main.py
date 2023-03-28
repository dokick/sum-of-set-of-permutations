from itertools import permutations
from math import factorial
from typing import Iterable


def tuple_as_int(tup: tuple[int, ...]) -> int:
    current_n = 0
    largest_degree = len(tup) - 1
    for idx, n in enumerate(tup):
        current_n += n * 10 ** (largest_degree - idx)
    return current_n


def sum_of_set(iterable: Iterable) -> int:
    result = 0
    for perm in permutations(iterable):
        result += tuple_as_int(perm)
    return result


def main() -> None:
    print(sum_of_set(range(1, 6)))  # 3.999.960
    print(66_666 * factorial(5) / 2)  # 3.999.960
    print(sum_of_set(range(1, 9)))  # 2.015.999.979.840
    print(99_999_999 * factorial(8) / 2)  # 2.015.999.979.840


if __name__ == "__main__":
    main()
