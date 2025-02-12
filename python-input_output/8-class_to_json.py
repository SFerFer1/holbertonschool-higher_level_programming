#!/usr/bin/python3
"""
This module defines a class named Rectangle.

Usage:
    You can create instances of Rectangle.
"""


import sys 


def class_to_json(obj):
    """
    This module defines a class named Rectangle.

    Usage:
    You can create instances of Rectangle.
    """
    obj_dict = {}
    for attribute, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            obj_dict[attribute] = value
    return obj_dict
