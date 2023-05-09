#!/usr/bin/python3
for nums in range(100):
    if int(nums / 10) != nums % 10 and int(nums / 10) < nums % 10:
        print("{}{}".format(int(nums / 10), nums % 10), end="")
        if (nums != 89):
            print(", ", end="")
print("")
