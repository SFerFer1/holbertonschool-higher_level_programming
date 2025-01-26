#!/usr/bin/python3
"""
Module: 3-say_my_name

This module contains
a single function that prints the name provided by the user.
The function ensures
that both the first name and last name are strings before
printing the formatted name

Function:
    - say_my_name:
      Prints "My name is <first_name> <last_name>" if inputs are valid.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or
        if size is a float less than 0.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size = 4:
        for index in range(size):
            print("#" * size)
    else:    
        for index in range(size):
            print("x" * size)

