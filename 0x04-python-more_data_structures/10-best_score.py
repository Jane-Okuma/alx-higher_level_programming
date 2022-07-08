#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        best = ""
        bestno = 0
        for i, j in a_dictionary.items():
            if j >= bestno:
                bestno = j
                best = i
        return best
