#!/usr/bin/python3
"""
This module defines a class named Rectangle.

Usage:
    You can create instances of Rectangle.
"""


import json


def load_from_json_file(filename):
    """
    This module defines a class named Rectangle.

    Usage:
    You can create instances of Rectangle.
    """
    with open(filename, 'r') as file:
        return json.load(file)
