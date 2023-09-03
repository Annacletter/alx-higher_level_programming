#!/usr/bin/python3
"""
Matrix Multiplication Module (NumPy Version)

This module defines a function to multiply two matrices using NumPy.
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Return the multiplication of two matrices.

    Args:
        m_a (numpy.ndarray): The first matrix.
        m_b (numpy.ndarray): The second matrix.

    Returns:
        numpy.ndarray: A new matrix representing the multiplication of m_a by m_b.
    """
    return np.matmul(m_a, m_b)

