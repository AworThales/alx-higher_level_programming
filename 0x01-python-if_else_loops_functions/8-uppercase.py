#!/usr/bin/python3
def uppercase(str):
    for k in range(len(str)):
        if ord(str[k]) >= 97 and ord(str[k]) <= 122:
            nums = 32
        else:
            nums = 0
        print("{:c}".format(ord(str[k]) - nums), end='')
    print()
