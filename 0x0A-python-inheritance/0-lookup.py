#!/usr/bin/python3
"""An object attribute lookup function."""


def lookup(obj):
    """Return The list of an object's available attributes."""
    return (dir(obj))
