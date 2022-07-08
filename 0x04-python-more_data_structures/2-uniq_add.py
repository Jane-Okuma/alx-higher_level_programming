#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    for i in range(0, len(my_list)):
        num = my_list[i]
        if num not in unique:
            unique.append(num)
    sum = 0
    for u in range(0, len(unique)):
        sum = sum + unique[u]
    return sum
