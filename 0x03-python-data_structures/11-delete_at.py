#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if length > 0:
        if idx < 0 or idx > length - 1:
            return my_list
        else:
            new_list = []
            for i in range(0, length):
                if i == idx:
                    continue
                else:
                    new_list.append(my_list[i])
            return new_list
