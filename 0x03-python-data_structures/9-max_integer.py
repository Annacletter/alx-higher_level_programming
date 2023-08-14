#!/usr/bin/python3
def max_integer(my_list=None):
    if my_list is None or not my_list:
        return None
    else:
        biggest = max(my_list)
        return biggest
