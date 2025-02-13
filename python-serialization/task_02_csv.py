#!/usr/bin/python3
"""
This module defines a class named Rectangle.

Usage:
    You can create instances of Rectangle.
"""


import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    
    except FileNotFoundError:
        print(f"Error: The file '{csv_filename}' was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

