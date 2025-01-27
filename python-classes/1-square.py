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
        """
        self._size = size