#!/usr/bin/python3
def pow(a, b):
    if a < 0 and b < 0:
        return abs(a ^ b)
    elif a < 0 or b < 0:
        return -(a ^ b)
    return a * b
