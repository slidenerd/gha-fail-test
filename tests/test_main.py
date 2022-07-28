"""Write tests for the main function."""

import pytest

from news.main import check_if_typeguard_works
from news.main import main


def test_main():
    """Check if main returns the correct value."""
    assert main() == 1


def test_typeguard():
    """This function will test if typeguard is working or not."""
    import json

    data = json.loads('{ "language": "wtf" }')
    with pytest.raises(TypeError):
        check_if_typeguard_works(data["language"])
