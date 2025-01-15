#!/usr/bin/python3
def islower(c):
    if ord(c)in range(97, 123):
        print("{} is lower".format(c))
        return True
    elif ord(c)in range(65, 91):
        print("{} is upper".format(c))
        return False
    else:
        return False
