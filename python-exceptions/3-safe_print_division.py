#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        total = a/b
        return total
    except (ZeroDivisionError, TypeError,):
        total = None
        return None
    finally:
        print("Inside result: {}".format(total)) 
