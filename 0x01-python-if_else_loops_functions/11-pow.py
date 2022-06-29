#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b > 1:
        mul = a
        for i in range(1, b):
            mul = mul * a
        return mul
    elif b < 1:
        mul = a
        b = b * -1
        for i in range(1, b):
            mul = mul * a
        return 1 / mul
