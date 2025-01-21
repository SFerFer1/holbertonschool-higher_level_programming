#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        ordenado = sorted(a_dictionary)
        for t in ordenado:
                print("{}: {}".format(t, a_dictionary[t]))
        
