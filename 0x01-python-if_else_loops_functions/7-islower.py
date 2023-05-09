#!/usr/bin/python3
def islower(c):
    ascii_nums = ord(c)
    if ascii_nums >= 97 and ascii_nums <= 122:
        return True
    return False
