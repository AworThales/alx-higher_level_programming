#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    t = len(sys.argv) - 1

    if t == 0:
        print("{} arguments.".format(t))
    elif t == 1:
        print("{} argument:".format(t))
    else:
        print("{} arguments:".format(t))

    if t >= 1:
        t = 0
        for arg in sys.argv:
            if t != 0:
                print("{}: {}".format(t, arg))
            t += 1
