#!/usr/bin/python3
Rectangle = __import__('11-rectangle').Rectangle
"""
This module defines a class Square that inherits from Rectangle.

Usage:
    You can create instances of Square by passing the size as an integer.
    The Square class allows you to calculate the area and print the square.

The class provides methods to check for type and value of the size.
"""

class Square(Rectangle):
    """
    Square class that inherits from the Rectangle class.

    It represents a square and provides functionality to calculate
    the area and a string representation of the square.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a new instance of Square.
        area(self): Returns the area of the square.
        __str__(self): Returns a string representation of the square.
    """

    def __init__(self, size):
        """
        Initializes the square with a specific size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than or equal to 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size <= 0:
            raise ValueError("size must be greater than 0")

        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
    
    def __str__(self):
        """
        Returns a string representation of the square.

        The string format will be "[Square] size/size".

        Returns:
            str: The string representation of the square.
        """
        return (f"[Square] {self.__size}/{self.__size}")
