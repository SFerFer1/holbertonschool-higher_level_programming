#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
   for i in a_dictionary:
      if a_dictionary[i].keys() == key:
            a_dictionary[i] = value