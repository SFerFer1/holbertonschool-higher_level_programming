#!/usr/bin/python3
"""
This module defines a class named Square.

This class have a size that is the length of the square.

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
    """
    def __init__(self, _Square__size):
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
