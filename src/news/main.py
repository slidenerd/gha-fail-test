"""The main module."""

import os
import sys
from datetime import datetime
from typing import Callable

add: Callable[[int, int], int] = lambda x, y: x + y


def main() -> int:
    """Entry point."""
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
    """A function to check if typeguard is running correctly."""
    return num
