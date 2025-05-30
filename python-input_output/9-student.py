#!/usr/bin/python3
"""
This module defines a class named Rectangle.

Usage:
    You can create instances of Rectangle.
"""


class Student:
    """
    This module defines a class named Rectangle.

    Usage:
    You can create instances of Rectangle.
    """
    def __init__(self, first_name, last_name, age):
        """
        This module defines a class named Rectangle.

        Usage:
        You can create instances of Rectangle.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        This module defines a class named Rectangle.

        Usage:
        You can create instances of Rectangle.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
            }
