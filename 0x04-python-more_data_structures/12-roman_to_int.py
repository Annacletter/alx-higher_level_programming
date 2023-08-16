#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                        'C': 100, 'D': 500, 'M': 1000}
    result = 0
    roman = roman_string
    
    if not isinstance(roman, str) or len(roman) == 0:
        return 0
    
    for index in range(len(roman)):
        if index < len(roman) - 1 and roman_dictionary[roman[index]] < roman_dictionary[roman[index + 1]]:
            result -= roman_dictionary[roman[index]]
        else:
            result += roman_dictionary[roman[index]]
    
    return result
This version of the code should work correctly for converting Roman numerals to integers.





Regenerate#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                        'C': 100, 'D': 500, 'M': 1000}
    result = 0
    roman = roman_string
    
    if not isinstance(roman, str) or len(roman) == 0:
        return 0
    
    for index in range(len(roman)):
        if index < len(roman) - 1 and roman_dictionary[roman[index]] < roman_dictionary[roman[index + 1]]:
            result -= roman_dictionary[roman[index]]
        else:
            result += roman_dictionary[roman[index]]
    
    return result
