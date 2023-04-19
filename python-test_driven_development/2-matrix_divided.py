#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(matrix) is not list or not all(
            type(row) is list for row in matrix):
        raise TypeError('matrix must be a matrix
                (list of lists) of integers/floats')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if matrix == []:
        return []
    n = len(matrix[0])
    if any(len(row) != n for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    return [[round(num / div, 2) for num in row] for row in matrix]
