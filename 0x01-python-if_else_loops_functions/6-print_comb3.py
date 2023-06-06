#!/usr/bin/python3
for i in range(10):
    for u in range(i+1, 10):
        if i == 8 and u == 9:
            print("{}{}" .format(i, u))
            break
        print("{}{}" .format(i, u), end=", ")
