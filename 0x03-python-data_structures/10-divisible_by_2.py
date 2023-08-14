#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    power_two = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            power_two.append(True)
        else:
            power_two.append(False)
    return (power_two)
