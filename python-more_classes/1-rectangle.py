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
        self._width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self._height = height

    @property
    def width(self):
        """Retrieve the size of the rectangle."""
        return self._width
    
    
    @property
    def height(self):
        """Retrieve the heigth of the rectangle."""
        return self._height
    
    @width.setter
    def width(self, value):
        """Set the width of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
