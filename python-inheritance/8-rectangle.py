#!/usr/bin/python3

"""
retun true if is of that class

Usage:
You can create instances of Rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """
    retun true if is of that class

    Usage:
    You can create instances of Rectangle.
    """

    def __init__(self, width, height):
        """
        retun true if is of that class

        Usage:
        You can create instances of Rectangle.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be greater than 0")
        
        if height <= 0:
            raise ValueError("height must be greater than 0")

        self.__width = width
        self.__height = height
