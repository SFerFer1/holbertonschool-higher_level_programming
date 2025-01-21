#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for i in range(0, len(a_dictionary)):
        if i == key:
            a_dictionary.pop(i)
            return