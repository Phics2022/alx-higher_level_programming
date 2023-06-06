#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 122:
            upper_i = chr(ord(i) - 32)
            print("{}" .format(upper_i), end="")
        else:
            print("{}" .format(i), end="")
    print()
