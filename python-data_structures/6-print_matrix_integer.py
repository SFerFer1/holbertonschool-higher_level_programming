#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
     for lista in matrix:
        print(" ".join("{}".format(num)for num in lista))