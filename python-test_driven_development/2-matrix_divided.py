#!/usr/bin/python3
def matrix_divided(matrix, div):
    # check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # check if all rows are the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # check if div is equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # create new matrix with division of each element by div
    new_matrix = [[round(element/div, 2) for element in row] for row in matrix]

    return new_matrix
