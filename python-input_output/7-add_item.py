#!/usr/bin/python3
"""
This module defines a class named Rectangle.

Usage:
    You can create instances of Rectangle.
"""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def main():
    """
    This module defines a class named Rectangle.

    Usage:
    You can create instances of Rectangle.
    """
    arguments = sys.argv[1:]
    
    try:
        existing_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_items = []

    existing_items.extend(arguments)

    save_to_json_file(existing_items, "add_item.json")

if __name__ == "__main__":
    main()
