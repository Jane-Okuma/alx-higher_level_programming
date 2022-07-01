#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    if length == 0:
        print("{:d}".format(0))
    elif length > 1:
        sum = 0
        for i in range(0, length):
            sum = sum + int(argv[i + 1])
        print("{:d}".format(sum))
