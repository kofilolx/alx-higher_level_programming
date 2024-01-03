#!/usr/bin/python3
def uppercase(str):
    for j in str:
        j = ord(j)
        if j >= 97 and j <= 122:
            j -= 32
        j = chr(j)
        print("{}".format(j), end='')
    print("")
