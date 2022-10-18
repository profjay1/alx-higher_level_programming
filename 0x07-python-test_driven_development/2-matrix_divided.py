#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
The 2-matrix_divided module supplies one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """
        Divides all elements of a matrix
    """
    if any(len(i) != len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    for row in matrix:
        if len(row) == 0 or type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")
    try:
        res = [[round(value / div, 2) for value in row] for row in matrix]
    except TypeError:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    return res


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
