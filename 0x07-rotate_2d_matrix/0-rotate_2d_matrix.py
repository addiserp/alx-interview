#!/usr/bin/python3
"""
    For the “0. Rotate 2D Matrix” project
"""


def rotate_2d_matrix(matrix):
    """
        an in-place algorithm to rotate an n x n 2D matrix by
        90 degrees clockwise.
    """
    for x, y in enumerate(zip(*reversed(matrix))):
        matrix[x] = list(y)


if __name__ == '__main__':
    gmat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    """
    Given an n x n rotate_2d_matrix(gmat),
    rotate it 90 degrees clockwise.
    """
    rotate_2d_matrix(gmat)
    for i in gmat:

        for j in i:
            if j == i[-1]:
                print('{:d}'.format(j), end='')
            else:
                print('{:d}'.format(j), end=' ')
        print()
