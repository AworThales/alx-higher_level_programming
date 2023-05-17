#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    record_keys = list(a_dictionary.keys())

    for value_dictn in record_keys:
        if value == a_dictionary.get(value_dictn):
            del a_dictionary[value_dictn]

    return (a_dictionary)
