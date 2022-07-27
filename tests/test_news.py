"""Write tests for the version number."""

from news import __version__


def test_version():
    """Check if the correct version is returned."""
    assert __version__ == "0.1.0"
