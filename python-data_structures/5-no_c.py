#!/usr/bin/python3
def no_c(my_string):
    ret = ""
    i = 0
    while i in my_string:
        if i != "c" and i != "C":
            ret += i
    return ret
