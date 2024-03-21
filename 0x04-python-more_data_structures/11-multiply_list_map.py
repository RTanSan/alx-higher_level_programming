#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    m = lambda x: x * number
    n = map(m, my_list)
    return list(n)
