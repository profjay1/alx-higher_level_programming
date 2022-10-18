#!/usr/bin/python3
"""
This is the "101-lazy_matrix_mul" module.
The 101-lazy_matrix_mul module supplies one function, lazy_matrix_mul(m_a, m_b).
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
        Multiplies two matrices.
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
    m_a_notrect = False
    m_b_notrect = False
    m_a_notnum = False
    m_b_notnum = False
    m_a_scalar = False
    m_b_scalar = False

    # check matrix a
    for row in m_a:
        if type(row) is not list:
            m_a_scalar = True
        if len(row) != len(m_a[0]):
            m_a_notrect = True
        for num in row:
            if type(num) not in (int, float):
                m_a_notnum = True

    # check matrix b
    for row in m_b:
        if type(row) is not list:
            m_b_scalar = True
        if len(row) != len(m_b[0]):
            m_b_notrect = True
        for num in row:
            if type(num) not in (int, float):
                m_b_notnum = True

    if m_a_scalar:
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if m_b_scalar:
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if m_a_notnum:
        raise TypeError("invalid data type for einsum")
    if m_b_notnum:
        raise TypeError("invalid data type for einsum")
    if m_a_notrect:
        raise ValueError("setting an array element with a sequence.")
    if m_b_notrect:
        raise ValueError("setting an array element with a sequence.")

    return np.matrix(m_a) * np.matrix(m_b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
