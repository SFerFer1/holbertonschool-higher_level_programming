#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) not in range(97, 123) and :
            print("{}".format((i)), end="")
        else:
            print("{}".format(chr(ord(i) - 32)))
