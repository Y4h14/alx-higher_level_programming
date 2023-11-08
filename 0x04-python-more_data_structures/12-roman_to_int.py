#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return (0)
    result = 0
    prev = 0
    letters = {"I": 1, "V": 5, "X": 10,
               "L": 50, "D": 500, "C": 100, "M": 1000}
    for k in reversed(roman_string):
        value = letters[k]

        if value < prev:
            result -= value
        else:
            result += value
        prev = value

    return (result)
