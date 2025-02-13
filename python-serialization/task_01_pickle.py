#!/usr/bin/python3
"""
This module defines a class named Rectangle.

Usage:
    You can create instances of Rectangle.
"""
import pickle


class CustomObject:

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            if os.path.getsize(filename) == 0:
            raise ValueError("File is empty")
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Object serialized and saved to {filename}")
        except Exception as e:
            print(f"Error occurred while serializing: {e}")

    @classmethod
    def deserialize(cls, filename: str):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Error occurred while deserializing: {e}")
            return None