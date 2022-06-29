#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if a == 8 and b == 9:
            print("{0}{1}".format(a, b))
            break
        elif a > b:
            continue
        elif a < b:
            print("{0}{1}".format(a, b), end=", ")
