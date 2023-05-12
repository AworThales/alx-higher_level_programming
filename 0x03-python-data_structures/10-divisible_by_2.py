#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    finds_div = []

    for t in range(len(my_list)):
        if my_list[t] % 2 == 0:
            finds_div.append(True)
        else:
            finds_div.append(False)

    return (finds_div)
