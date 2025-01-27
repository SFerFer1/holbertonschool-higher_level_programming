#!/usr/bin/python3
class Square:
    """
    clase Square represante a square.
        Attributes:
        _size (int or float): The size (length) of one side of the square.

    Methods:
        __init__(size): Constructor that initializes the size of the square.
    """
    

    def area(self):
        """
        Calcualte the area.

        Returns:
            the area of the square
        """
        return self._size ** 2

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self._size
    
    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

