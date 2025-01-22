#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        total = a/b
        return total
    except IndexError:
        total = None
        pass 
    except Exception:
        total = None
        pass
    finally:
        print("Inside result: {}".format(total))
