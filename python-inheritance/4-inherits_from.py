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
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
