#!/usr/bin/python3
def no_c(my_string):
    string_list = []
     new_string = ""
    for i in range(0, len(my_string)):
        string_list.append(my_string[i])
    for i in range(0, len(string_list)):
        if string_list[i] == "C" or string_list[i] == "c":
            continue
        else:
                    new_string = new_string + string_list[i]
    return(new_string)
