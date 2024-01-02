#!/usr/bin/python3
"""Prints the lowercase alphabet without a new line."""

for ascii_code in range(97, 123):
    print("{}".format(chr(ascii_code)), end="")
