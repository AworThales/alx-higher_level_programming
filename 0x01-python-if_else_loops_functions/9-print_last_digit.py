#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last_nums = number % 10
    else:
        last_nums = number % -10
        last_nums *= -1

    print("{:d}".format(last_nums), end='')
    return (last_nums)
