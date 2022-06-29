#!/usr/bin/python3
for i in range(122, 98):
    if i % 2 == 0:
        code = i
    else:
        code = i + 32
    print("{}".format(chr(i)), end="")
