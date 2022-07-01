#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    if length == 0:
        print("{:d} arguments.".format(length))
    elif length == 1:
        print("{:d} argument:".format(length))
        print("1: {:s}".format(argv[1]))
    elif length > 1:
        print("{} arguments:".format(length))
        for i in range(0, length):
            print("{:d}: {:s}".format(i + 1, argv[i + 1]))
