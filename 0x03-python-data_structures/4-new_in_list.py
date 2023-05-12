#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    distance = len(my_list)

    fresh_list = my_list[:]

    if 0 <= idx < distance:
        fresh_list[idx] = element

    return (fresh_list)
