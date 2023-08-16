#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared_row = [x * x for x in row]
        squared_matrix.append(squared_row)
    return squared_matrix
