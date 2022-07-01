#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    length = len(argv) - 1
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print("{:d}".format(1))
    elif argv[2] == "+" or argv[2] == "-" or argv[2] == "*" or argv[2] == "/":
        print("Unknown operator. Available operators: +, -, * and /")
        print("{:d}".format(1))
    else:
        a = int(argv[1])
        b = int(argv[3])
        c = argv[2]
        if c == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
            print("{:d}".format(0))
        elif c == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
            print("{:d}".format(0))
        elif c == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
            print("{:d}".format(0))
        elif c == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
            print("{:d}".format(0))
