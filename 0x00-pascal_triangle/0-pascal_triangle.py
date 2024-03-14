#!/usr/bin/python3
"""
    a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
        -Returns an empty list if n <= 0
        -You can assume n will be always an integer
    """
    resvale = []
    if n > 0:
        for i in range(1, n + 1):
            lev = []
            CC = 1
            for j in range(1, i + 1):
                lev.append(CC)
                CC = CC * (i - j) // j
            resvale.append(lev)
    return resvale
