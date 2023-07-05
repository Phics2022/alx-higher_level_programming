#!/usr/bin/python3
""" This module divides a matrix """


def matrix_divided(matrix, div):
    """ This function divide a matrix
    Args:
    matrix(list): matrix aka list of list
    div(int): divisor

    Return:
    list: The new list containing the divide elements

    Raise:
    TypeError: when the matrix is not a list of lists
    and the div is not an int or float
    ZeroDivisionError: when div is 0
    """
    # check if matrix is a list of lists
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(err_msg)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(err_msg)
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError(err_msg)

    # check if each row is of the same size
    def_length = len(matrix[0])
    if not all(len(row) == def_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # check if div is an int or float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # run the code
    new_matrix = []
    for row in matrix:
        value = [round(element / div, 2) for element in row]
        new_matrix.append(value)
    return new_matrix
