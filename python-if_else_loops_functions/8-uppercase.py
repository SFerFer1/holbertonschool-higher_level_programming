#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if 97 <= ord(i) <= 122:
            result += "{}".format(chr(ord(i) - 32))
        else:
            result += "{}".format(i)
    print(result)
