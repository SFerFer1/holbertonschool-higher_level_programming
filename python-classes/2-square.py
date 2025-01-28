#!/usr/bin/python3
class Square:
    """
    clase Square represante a square.
        Attributes:
        _size (int or float): The size (length) of one side of the square.

    Methods:
        __init__(size): Constructor that initializes the size of the square.
    """
    def __init__(self, size):
        """
        Constructor of class Square.
        
        set Square instances

        Parameters:
            size (int or float): The size of one side of the square.
        
        Raise:
            TypeError: when size is no an integer
            ValueError: when size is negative 
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
