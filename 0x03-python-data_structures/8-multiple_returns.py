#!/usr/bin/python3
def multiple_returns(sentence):
    my_ordered_list = ()
    if len(sentence) == 0:
        my_ordered_list = 0, "None"
    else:
        my_ordered_list = len(sentence), sentence[0]
    return my_ordered_list
