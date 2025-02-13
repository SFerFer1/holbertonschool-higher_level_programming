#!/usr/bin/python3
"""
This module defines a class named Rectangle.

Usage:
    You can create instances of Rectangle.
"""


def pascal_triangle(n):
    """
    This module defines a class named Rectangle.

    Usage:
    You can create instances of Rectangle.
    """
    if n <= 0:
        return []
    
    tri = []
    
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = tri[i - 1][j - 1] + tri[i - 1][j]
        tri.append(row)
    
    return tri
