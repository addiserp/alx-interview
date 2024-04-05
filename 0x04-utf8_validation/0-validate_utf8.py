#!/usr/bin/python3
"""
    a method that determines if a given data set represents
    a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
        to validate if a valid UTF-8 encoding is
        in a given data set represents
    """
    nbytes = 0
    for num in data:
        mask = 1 << 7
        if nbytes == 0:
            while mask & num:
                nbytes += 1
                mask >>= 1
            if nbytes == 0:
                continue
            if nbytes == 1 or nbytes > 4:
                return False
        else:
            if not (num & (1 << 7) and not (num & (1 << 6))):
                return False
        nbytes -= 1
    return nbytes == 0
