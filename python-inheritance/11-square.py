#!/usr/bin/python3
"""ashhsjjdi dsoidu saisdsio"""
Rectangle = __import__('11-rectangle').Rectangle


class Square(Rectangle):
    """
    retun true if is of that class

    Usage:
    You can create instances of Rectangle.
    """
    def __init__(self, size):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size <= 0:
            raise ValueError("size must be greater than 0")

        self.__size = size

    def area(self):
        return self.__size ** 2
    
    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
