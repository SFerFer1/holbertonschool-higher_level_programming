#!/usr/bin/python3
"""
This module defines a class named Rectangle.

Usage:
    You can create instances of Rectangle.
"""


def append_write(filename="", text=""):
    """
    This module defines a class named Rectangle.

    Usage:
    You can create instances of Rectangle.
    """
    with open(filename, 'a', encoding='utf-8') as a:
        return a.write(text)
