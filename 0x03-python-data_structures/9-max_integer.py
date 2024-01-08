#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        roof_int = my_list[0]
        for j in range(len(my_list)):
            if my_list[j] > roof_int:
                roof_int = my_list[j]
        return roof_int
