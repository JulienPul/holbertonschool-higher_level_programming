#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}
    numbers = list(map(values.get, roman_string))
    result = 0
    result = result + numbers
    result = roman_to_int
    return roman_to_int
