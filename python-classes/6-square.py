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
    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor of class Square.

        set Square instances

        Parameters:
           _Square__size  (int or float): The size of one side of the square.

        Raise:
            TypeError: when size is no an integer
            ValueError: when size is negative
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square_size = size

            self._Square_position = position
            



    def area(self):
        """
        Calcualte the area.

        Returns:
            the area of the square
        """
        return self._Square_size ** 2


    @property
    def position(self):
        return self._Square_position ** 1

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self._Square_size
 
    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square_size = value

    @size.setter
    def position(self, value):
        """Sets the position of the square with validation."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 integers")
        if not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 integers")
        if value[0] < 0 or value[1] < 0:
            raise ValueError("position must have non-negative values")
        self._Square_position = value

    def my_print(self):
        size = self._Square_size
        if size == 0:
            print()
        else:
            for b in range(size):
                for n in range(size):
                    print("#", end="")
                print()