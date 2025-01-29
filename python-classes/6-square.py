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
        self.size = size
        if (not isinstance(position, tuple) or len(position) != 2 or
            not all(isinstance(i, int) and i >= 0 for i in position)):
                mensaje = "position must be a tuple of 2 positive integers"
                raise TypeError(mensaje)

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
        """Retrieve the size of the square."""
        return self._Square_position

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

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._Square_position = value

    def my_print(self):
        size = self._Square_size
        if size == 0:
            print()
        else:
            for y in range(self.position[1]):
                print()
            for n in range(size):
                for x in range(self.position[0]):
                    print(" ", end="")
                print("#" * self.size)
