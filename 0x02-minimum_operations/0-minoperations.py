#!/usr/bin/python3
"""
    a method that calculates the fewest number of operations needed to
    result in exactly n H characters in the file. Copy All and Paste.
    Given a number n
"""


def minOperations(x):
    """
    a method that calculates the fewest number of operations needed to
    result in exactly n H characters in the file. Copy All and Paste.
    Given a number n
    Args:
        x: value input
        flist: List to truck the operations
    Return: the sum of the operations
    """
    if x < 2:
        return 0
    flist = []
    i = 1
    while x != 1:
        i += 1
        if x % i == 0:
            while x % i == 0:
                x /= i
                flist.append(i)
    return sum(flist)
