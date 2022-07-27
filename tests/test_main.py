"""Write tests for the main function."""

from news.main import main


def test_main():
    """Check if main returns the correct value."""
    assert main() == 1
