#!/usr/bin/python3
def max_integer(my_list=[]):
    my_length = len(my_list)

    if my_length == 0:
        return (None)

    maximum_int = my_list[0]

    for i in range(1, my_length):
        if my_list[i] > maximum_int:
            maximum_int = my_list[i]

    return (maximum_int)
