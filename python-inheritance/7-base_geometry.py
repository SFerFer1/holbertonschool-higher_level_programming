#!/usr/bin/python3
"""
retun true if is of that class

Usage:
You can create instances of Rectangle.
"""
class BaseGeometry:
    """
    retun true if is of that class

    Usage:
    You can create instances of Rectangle.
    """
    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """positive"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
