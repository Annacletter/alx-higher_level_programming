#!/usr/bin/python3
def roman_to_int(roman_string):
        roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                            'C': 100, 'D': 500, 'M': 1000}
        answer = 0
        component = 0
        roman = roman_string
        if type(roman) is not str or len(roman) is 0:
                return 0
        for component in range(component, len(roman)):
                if component < len(roman) - 1\
                   and\
                   roman_dictionary[roman[component]] <\
                   roman_dictionary[roman[component + 1]]:
                    answer -= roman_dictionary[roman[component]]
                else:
                    answer += roman_dictionary[roman[component]]
        return answer
