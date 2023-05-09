#!/usr/bin/python3
def remove_char_at(str, n):
    t = 0
    new_string = ""
    for k in str:
        if t != n:
            new_string += k
        t += 1
    return new_string
