"""The main module."""

import os
import sys
from datetime import datetime
from typing import Callable

add: Callable[[int, int], int] = lambda x, y: x + y


def main() -> int:
    """Entry point.

    Returns:
        The sum of 0 and 1
    """
    print(
        "hello from news, you have",
        os.cpu_count(),
        "cpus on",
        datetime.now(),
        "running",
        sys.version,
    )
    return add(0, 1)


def check_if_typeguard_works(num: int) -> int:
    """A function to check if typeguard is running correctly.

    Args:
        num (int): Any number

    Returns:
        int: The number that was passed in
        The number that was passed in
    """
    return num
