#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in range(len(matrix)):
        for x in range(len(matrix[n])):
            print('{:d}'.format(matrix[n][x]), end='')
            if x != (len(matrix[n]) - 1):
                print(' ', end='')
        print('')
