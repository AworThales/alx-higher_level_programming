#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for t in range(len(matrix)):
        for h in range(len(matrix[t])):
            if h != 0:
                print(" ", end='')
            print("{:d}".format(matrix[t][h]), end='')
        print()
