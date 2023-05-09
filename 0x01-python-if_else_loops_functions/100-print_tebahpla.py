#!/usr/bin/python3
for t in reversed(range(97, 123)):
    print("{:c}".format(t if (t % 2 == 0) else (t - 32)), end='')
