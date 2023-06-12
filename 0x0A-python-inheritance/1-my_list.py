#!/usr/bin/python3
"""An inherited list class MyList."""


class MyList(list):
    """Implementing sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print the list in sorted ascending order."""
        print(sorted(self))
