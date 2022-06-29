#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        code = int(i)
    else:
        code = int(i) - 32
    print("{:s}".format(chr(code)), end="")
