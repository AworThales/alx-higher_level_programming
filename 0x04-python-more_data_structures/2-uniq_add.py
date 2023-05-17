#!/usr/bin/python3
def uniq_add(my_list=[]):
    special_list = set(my_list)
    numb = 0

    for t in special_list:
        numb += t

    return (numb)
