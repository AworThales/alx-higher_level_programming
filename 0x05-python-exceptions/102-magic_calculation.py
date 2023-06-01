#!/usr/bin/python3
def magic_calculation(a, b):
    answ = 0
    for t in range(1, 3):
        try:
            if t > a:
                raise Exception('Too far')
            answ += a ** b / t
        except Exception:
            answ = b + a
            break
    return answ
