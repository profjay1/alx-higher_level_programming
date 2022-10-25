#!/usr/bin/python3
''' Module for pascal_triangle func '''


def pascal_triangle(n):
    ''' Returns list that represents a pascal triangle of n size '''

    if (n <= 0):
        return []

    triangle = [[1]]

    for row in range(n - 1):  # subtract 1 since we initialize the list with 1
        prev_row = [0] + triangle[-1] + [0]
        tmp = []
        for i in range(len(triangle[-1]) + 1):
            tmp.append(prev_row[i] + prev_row[i + 1])
        triangle.append(tmp)

    return triangle
