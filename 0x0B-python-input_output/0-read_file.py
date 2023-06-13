#!/usr/bin/python3
"""A text file-reading function."""


def read_file(filename=""):
    """Print contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as ft:
        print(ft.read(), end="")
