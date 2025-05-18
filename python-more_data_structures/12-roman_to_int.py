#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    values = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
              'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
    numbers = list(map(values.get, roman_string))
    for i in values:
        result = 0
        result = sum(numbers)
        new_list = []
        new_list = roman_string.append(result)
    return new_list
