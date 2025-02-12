#!/usr/bin/python3
import json
"""
This module defines a class named Rectangle.

Usage:
    You can create instances of Rectangle.
"""


def load_from_json_file(filename):
    """
    This module defines a class named Rectangle.

    Usage:
    You can create instances of Rectangle.
    """
    with open(filename, 'r') as file:
        return json.load(file)