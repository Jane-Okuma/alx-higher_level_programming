#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        tuple_a[1] = 0
    if len(tuple_a) == 0:
        tuple_a[0] = tuple_b[1] = 0
    if len(tuple_b) == 1:
        tuple_b[1] = 0
    if len(tuple_b) == 0:
        tuple_b[0] = tuple_b[1] = 0

    sum_0 = tuple_a[0] + tuple_b[0]
    sum_1 = tuple_a[1] + tuple_b[1]
    ls = []
    ls.append(sum_0)
    ls.append(sum_1)
    t1 = tuple(ls)
    return t1
