#!/usr/bin/python3
"""
0. Change comes from within 
"""


def makeChange(coins, total):
    """
    This Will determine the fewest number of coins needed to meet
    a given amount total.

    Args:
        coins ([List]): [Coins list available]
        total ([int]): [amount needed in total]
    """
    if total <= 0:
        return 0
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            temp += 1
        if check == total:
            return temp
        check -= i
        temp -= 1
    return -1
