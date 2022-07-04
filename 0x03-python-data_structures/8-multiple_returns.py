#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        firstchar = None
    else:
        firstchar = sentence[0]
    t1 = (length, firstchar)
    return t1
