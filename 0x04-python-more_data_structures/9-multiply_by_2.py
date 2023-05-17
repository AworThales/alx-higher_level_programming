#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    curren_dir = a_dictionary.copy()
    records_keys = list(curren_dir.keys())

    for t in records_keys:
        curren_dir[t] *= 2

    return (curren_dir)
