#!/usr/bin/python3
"""Prints the lowercase alphabet without a new line, excluding 'q' and 'e'."""

for ascii_code in range(97, 123):
    if chr(ascii_code) not in ['q', 'e']:
        print("{}".format(chr(ascii_code)), end="")
