#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordenado = sorted(a_dictionary)
    for i in ordenado:
        print("{} {}".format(i, ordenado[i]))
