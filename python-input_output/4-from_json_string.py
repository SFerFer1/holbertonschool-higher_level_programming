#!/usr/bin/python3
import json
"""
This module defines a class named Rectangle.

Usage:
    You can create instances of Rectangle.
"""


def from_json_string(my_str):
    return (json.load(my_str))