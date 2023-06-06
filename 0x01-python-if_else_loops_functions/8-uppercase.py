#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 122:
            upper_i = chr(ord(i) - 32)
        else:
            upper_i = i
        print("{}" .format(upper_i), end="")
    print()
