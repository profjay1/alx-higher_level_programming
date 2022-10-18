#!/usr/bin/python3
"""
This is the "100-matrix_mul" module.
The 100-matrix_mul module supplies one function, matrix_mul(m_a, m_b).
"""


def matrix_mul(m_a, m_b):
    """
        Multiplies 2 matrices
        Args:
            m_a: the first matrix
            m_b: the second matrix
        Returns:
            matrix: the product
        Raises:
            TypeError: If m_a or m_b are not lists.
            TypeError: If m_a or m_b are not lists of lists.
            ValueError: If m_a or m_b are empty lists/matrices.
            TypeError: If m_a or m_b contain a non int/float.
            TypeError: If m_a or m_b are not rectangular.
            ValueError: If m_a or m_b can't be multiplied.
    """
    
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    m_a_notrect = False
    m_b_notrect = False
    m_a_notnum = False
    m_b_notnum = False

    # check matrix a
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            m_a_notrect = True
        for num in row:
            if type(num) not in (int, float):
                m_a_notnum = True

    # check matrix b
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            m_b_notrect = True
        for num in row:
            if type(num) not in (int, float):
                m_b_notnum = True

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if m_a_notnum:
        raise TypeError("m_a should contain only integers or floats")

    if m_b_notnum:
        raise TypeError("m_b should contain only integers or floats")

    if m_a_notrect:
        raise TypeError("each row of m_a must be of the same size")

    if m_b_notrect:
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = [[] for i in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            c = 0
            for k in range(len(m_b)):
                c += m_a[i][k] * m_b[k][j]
            res[i].append(c)

    return res

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
