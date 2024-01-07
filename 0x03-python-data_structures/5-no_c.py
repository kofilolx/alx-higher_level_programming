#!/usr/bin/python3
def no_c(my_string):
    current_string = my_string.translate({ord(i): None for i in 'cC'})
    return current_string
