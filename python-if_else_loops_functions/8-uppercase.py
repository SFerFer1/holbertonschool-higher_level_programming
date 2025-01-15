#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(str[i]) in range(97, 123):
            print("{}".format(i-32))
        else:
            print("{}".format(i))
    
