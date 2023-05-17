#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    records_ord = list(a_dictionary.keys())
    records_ord.sort()
    for t in records_ord:
        print("{}: {}".format(t, a_dictionary.get(t)))
