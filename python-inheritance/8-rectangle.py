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

        if width or height > 0:
            return 0

        self.__width = width
        self.__height = height