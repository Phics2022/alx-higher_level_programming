#!/usr/bin/python3
import sys
if __name__ == "__main__":
    a = 0
    b = 0
    for a in range(1, len(sys.argv)):
        b += int(sys.argv[a])
    print(b)
