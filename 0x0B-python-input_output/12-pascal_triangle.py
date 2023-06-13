#!/usr/bin/python3
"""A Pascal's Triangle function."""


def pascal_triangle(n):
    """Representing Pascal's Triangle of size n.
    Returns list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triang = [[1]]
    while len(triang) != n:
        trian = triang[-1]
        tmp = [1]
        for i in range(len(trian) - 1):
            tmp.append(trian[i] + trian[i + 1])
        tmp.append(1)
        triang.append(tmp)
    return triang
