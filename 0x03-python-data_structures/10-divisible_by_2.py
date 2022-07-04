#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) > 0:
        list2 = []
        for i in range(0, len(my_list)):
            if my_list[i] % 2 == 0:
                check = True
            else:
                check = False
            list2.append(check)
        return list2
