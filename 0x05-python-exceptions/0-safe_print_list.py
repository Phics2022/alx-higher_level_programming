#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for y in range(x - 1):
        try:
            z = my_list[y]
        except:
            pass
        else:
            count += 1
            print("{z}", end="")
    print()
    return count

