#!/usr/bin/python3
#print the alphatbet in reverse in this oder zYxW
#loop int small letters
#for every loop we want to change to Capital
n = 0
y = 0
for i in range(122, 96, -1):
    if y % 2 == 0:
        n = 0
    else:
        n = 32
    print("{:c}" .format(i - n), end="")
    y += 1
