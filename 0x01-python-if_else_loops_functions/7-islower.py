#!/usr/bin/python3

"""clas definiton islower"""
def islower(c):
    check = ord(c)
    if check >= 97 and check <= 122:
        return True
    else:
        return False
