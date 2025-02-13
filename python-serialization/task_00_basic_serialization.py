#!/usr/bin/python3
"""
This module defines a class named Rectangle.

Usage:
    You can create instances of Rectangle.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    This module defines a class named Rectangle.

    Usage:
    You can create instances of Rectangle.
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

data = {'name': 'John', 'age': 30, 'city': 'New York'}
serialize_and_save_to_file(data, 'output.json')



def load_and_deserialize(filename):
    """
    This module defines a class named Rectangle.

    Usage:
    You can create instances of Rectangle.
    """
    with open(filename, 'r') as file:
        ret = json.load(file)
        return ret


