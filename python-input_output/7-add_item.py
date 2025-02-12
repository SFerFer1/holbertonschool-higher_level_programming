#!/usr/bin/python3
import sys
import os 
sys.path.append(os.getcwd())

from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file
def main():

    try:
        current_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        current_list = []

    current_list.extend(sys.argv[1:])

    save_to_json_file(current_list, "add_item.json")

if __name__ == "__main__":
    main()
