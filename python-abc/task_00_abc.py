#!/usr/bin/python3
"""
This module defines a class named Rectangle.

Usage:
    You can create instances of Rectangle.
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    This module defines a class named Rectangle.

    Usage:
        You can create instances of Rectangle.
    """

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"