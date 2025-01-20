#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    find = my_list[0]
    for num in my_list:
        if num > find:
            find = num
    print("Max: {}".format(find))
    return find
