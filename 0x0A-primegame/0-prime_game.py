#!/usr/bin/python3
"""
    The challenge involves determining the winner of a game based on the
    strategic removal of prime numbers and their multiples from a set of
    consecutive integers.
"""


def rm_multiples(ls, x):
    """
        removing that number and its multiples from the set.
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break


def isWinner(x, nums):
    """
        x is the number of rounds and nums is an array of n.
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None
