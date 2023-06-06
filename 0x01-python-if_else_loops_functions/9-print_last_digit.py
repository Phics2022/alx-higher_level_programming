#!/usr/bin/python3
def print_last_digit(number):
    true_number = number
    if number < 0:
        true_number = number * -1
    last_digit = true_number % 10
    print("{}" .format(last_digit), end="")
    return last_digit
