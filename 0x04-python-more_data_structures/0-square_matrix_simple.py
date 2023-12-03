#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = [[element ** 2 for element in row] for row in matrix]
    return result_matrix
