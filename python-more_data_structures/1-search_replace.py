#!/usr/bin/python3
def search_replace(my_list, search, replace):
    temp = my_list[:]
    for i in temp:
        for n in i:
            if n == search:
                n = replace
    return temp
