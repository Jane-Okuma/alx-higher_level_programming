#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = []
    new_dict = {}
    for i, j in a_dictionary.items():
        keys.append(i)
    for i in sorted(keys):
        new_dict[i] = a_dictionary[i]
    for i, j in new_dict.items():
        print("{}: {}".format(i, j))
