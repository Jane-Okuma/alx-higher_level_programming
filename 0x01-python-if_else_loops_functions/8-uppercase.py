#!/usr/bin/python3
def uppercase(str):
    count = 0
    for i in str:
        count = count + 1
        if ord(i) >= 97 and ord(i) <= 122:
            code = int(ord(i)) - 32
        else:
            code = int(ord(i))
        print("{}".format(chr(code)), end="")
        if count == len(str):
            print("\n")
