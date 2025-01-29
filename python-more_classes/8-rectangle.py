#!/usr/bin/python3
"""
This module defines a class named Rectangle.

Usage:
    You can create instances of Rectangle.
"""


class Rectangle:
    """
    A class representing a rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Constructor of class Square.

        set Square instances

        Parameters:
            width  (int): The width of the rectangle.
            height (int): The height of the rectangle.
        Raise:
            TypeError: when size is no an integer
            ValueError: when size is negative
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the size of the rectangle."""
        return self._Rectangle__width

    @property
    def height(self):
        """Retrieve the heigth of the rectangle."""
        return self._Rectangle__height

    @width.setter
    def width(self, value):
        """Set the width of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value

    def area(self):
        return self._Rectangle__height * self._Rectangle__width

    def perimeter(self):
        if self._Rectangle__height == 0 or self._Rectangle__width == 0:
            return 0
        return (self._Rectangle__height + self._Rectangle__width) * 2

    def __str__(self):
        string = ""
        if self._Rectangle__height == 0 or self._Rectangle__width == 0:
            return string
        else:
            for b in range(self._Rectangle__height):
                for n in range(self._Rectangle__width):
                    if not isinstance(self.print_symbol, str):
                        self.print_symbol = str(self.print_symbol)
                    string += self.print_symbol
                string += "\n"
            string = string[:-1]
        return string

    def __repr__(self):
        return "Rectangle({}, {})".format(
            self._Rectangle__width,
            self._Rectangle__height
        )

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if rect_1.area() >rect_2.area():
            return rect_1
        else:
            return rect_2