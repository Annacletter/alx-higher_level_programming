#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix and returns a new matrix.
    
    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int/float): The divisor.
    
    Returns:
        list: A new matrix with elements divided by div.
    
    Raises:
        TypeError: 
            - If matrix is not a list of lists of integers or floats.
            - If each row of the matrix is not the same size.
            - If div is not an int or float.
        ZeroDivisionError: If div is equal to 0.
    """
    # Check if matrix is a valid list of lists
    if (
        not isinstance(matrix, list) or 
        not matrix or 
        not all(isinstance(row, list) for row in matrix) or 
        not all(isinstance(ele, (int, float)) for row in matrix for ele in row)
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number and not zero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element by div and round to 2 decimal places
    return [[round(x / div, 2) for x in row] for row in matrix]
