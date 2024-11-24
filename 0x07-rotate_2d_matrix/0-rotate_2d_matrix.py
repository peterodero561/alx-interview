#!/usr/bin/python3
'''Rotating a 2D-matrix in Python'''


def rotate_2d_matrix(matrix):
    '''rotates a 2D-mtrix at 90 degrees clockwise'''
    n = len(matrix)
    # transpose
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse
    for row in matrix:
        row.reverse()
