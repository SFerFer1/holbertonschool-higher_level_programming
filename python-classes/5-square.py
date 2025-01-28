#!/usr/bin/python3
"""
This module defines a class named Square.

This class have a size that is the length of the square.

Attributes:
    _Square__size (int or float): The size of one side of the square

Methods:
    __init__(self, _Square__size):
        Initializes the square with a given size.

Usage:
    You can create instances of Square.
"""


class Square:
    """
    clase Square represante a square.
        Attributes:
        _size (int or float): The size (length) of one side of the square.

    Methods:
        __init__(size): Constructor that initializes the size of the square.
        def area(self): calculate the area of the square.
        def size(self): retrive the size of the square.

    """
    def __init__(self, _Square__size=0):
        """
        Constructor of class Square.

        set Square instances

        Parameters:
           _Square__size  (int or float): The size of one side of the square.

        Raise:
            TypeError: when size is no an integer
            ValueError: when size is negative
        """
        if not isinstance(_Square__size, int):
            raise TypeError("size must be an integer")
        if _Square__size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = _Square__size

    def area(self):
        """
        Calcualte the area.

        Returns:
            the area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self._Square__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def my_print(self):
        size = self._Square__size
        if size == 0:
            print()
        else:
            for b in range(size):
                for n in range(size):
                    print("#", end="")
                print()