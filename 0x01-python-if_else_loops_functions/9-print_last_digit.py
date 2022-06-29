#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -1 * number
        last_digit = number % 10
    else:
        print(number % 10)
        last_digit = number % 10
    return(last_digit)
