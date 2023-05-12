#!/usr/bin/python3
def no_c(my_string):
    distance = len(my_string)

    t = 0

    fresh_string = my_string[:]

    for h in range(distance):
        if (my_string[h] == 'c' or my_string[h] == 'C'):
            fresh_string = fresh_string[:(h - t)] + my_string[(h + 1):]
            t += 1

    return (fresh_string)
