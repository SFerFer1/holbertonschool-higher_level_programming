#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n = 0
    for i in my_list:
        if i%2 != 0:
            n = n+1
            print("{} is not divisible by 2".format(i))
        if i%2 == 0:
            print("{} is divisible by 2".format(i))
    if n != 0:
        return True
    else: 
        return False
