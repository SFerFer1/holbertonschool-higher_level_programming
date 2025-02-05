#!/usr/bin/python3
"""
This module defines a class named Rectangle.

Usage:
    You can create instances of Rectangle.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    This module defines a class named Rectangle.

    Usage:
        You can create instances of Rectangle.
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    This module defines a class named Rectangle.

    Usage:
        You can create instances of Rectangle.
    """
    def __init__(self, radius):
        self.__radius = radius


    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    This module defines a class named Rectangle.

    Usage:
        You can create instances of Rectangle.
    """
    def __init__(self, width, heigth):
        self.__width = width
        self.__heigth = heigth

    def area(self):
        return (self.__width * self.__heigth) 


    def perimeter(self):
        return ((self.__width * 2) + (self.__heigth * 2))

    def shape_info(shape):
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")