#!/usr/bin/python3
def roman_to_int(roman_string):
    r_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    prev = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    for rom in roman_string:
        val = r_dict[rom]
        if val > prev:
            result += val - prev * 2
        else:
            result += val
        prev = val
    return result
