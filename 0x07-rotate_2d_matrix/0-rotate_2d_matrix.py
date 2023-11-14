#!/usr/bin/python3
"""
    __description__:
        Rotate a 2D Array
"""


def rotate_2d_matrix(matrix):
    """Function to reverse a 2D array"""
    num = len(matrix)
    for i in range(num):
        for j in range(i, num):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    for row in matrix:
        row.reverse()
