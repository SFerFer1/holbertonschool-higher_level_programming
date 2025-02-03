#!/usr/bin/python3
class BaseGeometry:
    class Shape:
        def area(self):
            raise NotImplementedError("area() is not implemented")
