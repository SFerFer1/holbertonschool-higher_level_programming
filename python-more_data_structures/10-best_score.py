#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    bigger = 0
    for i in a_dictionary:
        if a_dictionary[i] > bigger:
            bigger = a_dictionary[i]
    for n in a_dictionary:
        if a_dictionary[n] == bigger:
            return n
