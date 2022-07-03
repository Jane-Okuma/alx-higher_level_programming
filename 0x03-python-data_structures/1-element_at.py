#!/usr/bin/python3
def elemet_at(my_list, idx):
    if idx < 0:
        return None
    range = len(my_list) - 1
    if idx > range:
        return None
    return my_list[idx]
