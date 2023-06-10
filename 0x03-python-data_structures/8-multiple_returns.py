#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        ret_tup = (len(sentence), None);
    else:
        ret_tup = (len(sentence), sentence[0])
    return ret_tup
