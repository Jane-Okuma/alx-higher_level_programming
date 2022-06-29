#!/usr/bin/python3
def uppercase(str):
    count = 0
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            code = int(ord(i)) - 32
            count = count + 1
        else:
            code = int(ord(i))
            count = count + 1
        print("{}".format(chr(code)), end="")
        if count == len(str) or len(str) == 0:
            print("{}".format("\n"), end="")
