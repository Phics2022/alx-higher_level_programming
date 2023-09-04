#!/usr/bin/python3
""" this module divides a matrix"""


def matrix_divided(matrix, div):
    """ This function divides matrix by div
    Args:
    matrix(list): The matrix to be divided
    div(int), (float): The divisor

    Return:
    List: The divided matrix
    """
    m = matrix
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a \
matrix (list of lists) of integers/floats")
    if not all(isinstance(r, list) and all(isinstance(v, (int, float)) for v in r) for r in m):
        raise TypeError("matrix must be a \
matrix (list of lists) of integers/floats")
    first = len(matrix[1])
    # check the row length
    for i in matrix:
        if len(i) != first:
            raise TypeError("Each row of the matrix \
must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # creating a new matrix
    length = len(matrix)
    new_matrix = []
    new_row = []
    for row in matrix:
        new_row = []
        for val in row:
            element = round(val / div, 2)
            new_row.append(element)
        new_matrix.append(new_row)
    return new_matrix
