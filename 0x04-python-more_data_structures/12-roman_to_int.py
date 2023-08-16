#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    if roman_string is None:
        return 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    leng = len(roman_string) - 1
    if roman_string[leng] not in roman:
        return 0
    number = roman[roman_string[leng]]
    for i in range(leng, 0, -1):
        if roman_string[i] not in roman:
            return 0
        now = roman[roman_string[i]]
        if roman_string[i - 1] not in roman:
            return 0
        prev = roman[roman_string[i - 1]]
        if i > 1:
            if roman_string[i - 2] not in roman:
                return 0
            if prev < now and roman[roman_string[i - 2]] <= prev:
                return 0
        if i > 2:
            if prev == now and roman[roman_string[i - 2]] == prev:
                if roman_string[i - 3] not in roman:
                    return 0
                if roman[roman_string[i - 3]] == roman[roman_string[i - 2]]:
                    return 0
        number += prev if prev >= now else - prev
    return number
