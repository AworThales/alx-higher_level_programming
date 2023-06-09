#!/usr/bin/python3
"""For square-printing function."""


def print_square(size):
    """Print the square with the # character.
    Args:
        size (int): A Height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for t in range(size):
        [print("#", end="") for g in range(size)]
        print("")
