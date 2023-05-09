#!/usr/bin/python3
for nums in range(100):
    if (nums != 99):
        print("{}{}, ".format(int(nums / 10), nums % 10), end="")
    else:
        print("{}{}".format(int(nums / 10), nums % 10))
