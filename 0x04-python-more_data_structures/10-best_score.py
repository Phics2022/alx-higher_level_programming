#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    key = ""
    if a_dictionary is None or len(list(a_dictionary)) == 0:
        return None
    for y, i in a_dictionary.items():
        if i > score:
            score = i
            key = y
    return key
