#!/usr/bin/python3
for word in range(26):
    if word != 4 and word != 16:
        print("{:s}".format(chr(word + ord("a"))), end="")
