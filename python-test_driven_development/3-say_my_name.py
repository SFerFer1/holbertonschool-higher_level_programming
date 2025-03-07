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


def say_my_name(first_name, last_name=""):
    """
    Prints a statement introducing the user by their first and last name.

    Args:
        first_name (str): The user's first name.
        last_name (str, optional): The user's last name. Defaults to an empty string.

    Raises:
        TypeError: If `first_name` or `last_name` are not strings.

    Prints:
        A statement in the format: "My name is <first_name> <last_name>".
        If `last_name` is not provided, the output will be: "My name is <first_name>".
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print("My name is {:s} {:s}".format(first_name, last_name))

