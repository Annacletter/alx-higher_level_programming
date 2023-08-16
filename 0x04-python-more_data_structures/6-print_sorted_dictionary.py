#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_items = sorted(a_dictionary.items())
    for key, value in sorted_items:
        print(f"{key}: {value}")
