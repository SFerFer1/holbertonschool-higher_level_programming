#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    n = 0
    for i in a_dictionary:
      if i.keys() == key:
            a_dictionary[i] = value
            n += 1
    if n  != 0:
        a_dictionary[key] = value
       

    