#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cont = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end ="")
            cont += 1
        except (TypeError, ValueError, IndexError) as e:
            print("Traceback (most recent call last):")
            print(f"  File \"<stdin>\", line {i+1}, in safe_print_list_integers")
            print(f"{e.__class__.__name__}: {str(e)}")
            continue
    print()
    return cont
