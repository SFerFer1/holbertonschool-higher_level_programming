#!/usr/bin/python3
def uniq_add(my_list=[]):
    only_unique = set(my_list)
    total = 0
    for i in only_unique:
        total += i
    return total
