#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    n = sorted(a_dictionary.keys())
    for key in n:
        print(f'{key}: {a_dictionary[key]}')
