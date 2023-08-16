#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    add = leng = 0
    for (a, b) in my_list:
        add += a * b
        leng += b
    return add / leng
