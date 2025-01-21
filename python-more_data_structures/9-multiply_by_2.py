#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        for i in a_dictionary:
            a_dictionary[i] = (a_dictionary[i] * 2)
    return a_dictionary
    