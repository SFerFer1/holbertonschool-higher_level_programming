#!/usr/bin/python3
"""
This module defines a class named Rectangle.

Usage:
    You can create instances of Rectangle.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    This module defines a class named Rectangle.

    Usage:
    You can create instances of Rectangle.
    """
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
