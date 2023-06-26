#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for y in range(x):
        try:
            z = my_list[y]
        except Exception:
            pass
        else:
            count += 1
            print(f"{z}", end="")
    print()
    return count
