"""The main module."""

import os
import sys
from datetime import datetime

add = lambda x, y: x + y


def main():
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
