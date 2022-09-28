#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_array = list()
    for i in range(0, len(matrix)):
        new_array.append(list(map(lambda x: x**2, matrix[i])))
    return new_array
