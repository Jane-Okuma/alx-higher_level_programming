#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence[0] == " ":
        firstchar = None
    else:
        firstchar = sentence[0]
    ls = []
    ls.append(length)
    ls.append(firstchar)
    t1 = tuple(ls)
    return t1
