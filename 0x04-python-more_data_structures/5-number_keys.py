#!/usr/bin/python3
def number_keys(a_dictionary):
    numb = 0
    records_keys = list(a_dictionary.keys())

    for i in records_keys:
        numb += 1

    return (numb)
