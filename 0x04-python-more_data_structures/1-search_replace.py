#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(range(len(my_list)))
    for i, n in enumerate(my_list):
        if n == search:
            new_list[i] = replace
        else:
            new_list[i] = n
    return new_list
