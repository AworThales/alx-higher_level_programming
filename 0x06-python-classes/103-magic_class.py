#!/usr/bin/python3

"""For a MagicClass matching exactly a bytecode."""

import math


class MagicClass:
    """For a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Bring the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Bring The circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
