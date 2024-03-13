#!/usr/bin/python3
'''
    a method that determines if all the boxes can be opened.
'''


def canUnlockAll(boxes):
    '''
    given that the first box is unlocked will checks if all the boxes in a
    list of boxes containing the keys (indices) to other boxes can be unlocked .
    '''
    nums = len(boxes)
    sboxs = set([0])
    uboxs = set(boxes[0]).difference(set([0]))
    while len(uboxs) > 0:
        boxIdx = uboxs.pop()
        if not boxIdx or boxIdx >= nums or boxIdx < 0:
            continue
        if boxIdx not in sboxs:
            uboxs = uboxs.union(boxes[boxIdx])
            sboxs.add(boxIdx)
    return nums == len(sboxs)
