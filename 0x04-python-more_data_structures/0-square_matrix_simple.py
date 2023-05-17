#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    current_matrix = matrix.copy()

    for t in range(len(matrix)):
        current_matrix[t] = list(map(lambda x: x**2, matrix[t]))

    return (current_matrix)
