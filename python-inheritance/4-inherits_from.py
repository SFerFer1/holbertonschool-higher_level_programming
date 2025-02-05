#!/usr/bin/python3
"""
retun true if is of that class

Usage:
You can create instances of Rectangle.
"""


def inherits_from(obj, a_class):
    """
    retun true if is of that class

    Usage:
    You can create instances of Rectangle.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
