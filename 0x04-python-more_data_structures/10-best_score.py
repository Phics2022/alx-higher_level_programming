#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    key = ""
    if len(a_dictionary) == 0 or a_dictionary is None:
        return None
    for y, i in a_dictionary.items():
        if i > score:
            score = i
            key = y
    return key
