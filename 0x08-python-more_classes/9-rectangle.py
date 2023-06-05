#!/usr/bin/python3
"""For Rectangle class."""


class Rectangle:
    """Staring a rectangle.
    Attributes:
        number_of_instances (int): Number of Rectangle instances.
        print_symbol (any): Symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """For a new Rectangle.
        Args:
            width (int): Width of the new rectangle.
            height (int): Weight of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting/setting the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting/setting the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Bring area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Bring perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Bring Rectangle with the greater area.
        Args:
            rect_1 (Rectangle): First Rectangle.
            rect_2 (Rectangle): Second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Bring a new Rectangle with width and height equal to size.
        Args:
            size (int): Width and height of the new Rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """Bring printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangular = []
        for t in range(self.__height):
            [rectangular.append(str(self.print_symbol)) for j in range(self.__width)]
            if t != self.__height - 1:
                rectangular.append("\n")
        return ("".join(rectangular))

    def __repr__(self):
        """Bring string representation of the Rectangle."""
        rectangular = "Rectangle(" + str(self.__width)
        rectangular += ", " + str(self.__height) + ")"
        return (rectangular)

    def __del__(self):
        """Print a message t every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
