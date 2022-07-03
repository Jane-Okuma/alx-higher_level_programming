#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    length = len(argv) - 1
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if argv[2] != "+" and argv[2] != "-" and argv[2] != "*" and argv[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
        
     a = int(argv[1])
     b = int(argv[3])
     c = argv[2]
     if c == "+":
         print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
     elif c == "-":
          print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
     elif c == "*":
          print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
     elif c == "/":
          print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
