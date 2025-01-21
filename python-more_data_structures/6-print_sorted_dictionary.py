#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordenado = sorted(a_dictionary)
    for t in ordenado:
        print("{}: {}".format(t, a_dictionary[t]))
        
