#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = [[0] * len(row) for row in matrix]
    for i, rows in enumerate(matrix):
        for n, j in enumerate(rows):
            new_list[i][n] = j * j

    return new_list
