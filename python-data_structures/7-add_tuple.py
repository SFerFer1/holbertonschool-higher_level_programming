#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    v1, v2 = (tuple_a + (0, 0))[:2]
    v11, v22 = (tuple_b + (0, 0))[:2]
    tuple_c = (v1 + v2, v11 + v22)
    return tuple_c
