#!/usr/bin/python3
"""Defines a function to check possibility of unlocking
    several locked boxes given the first box is always open
    and each box may contain keys to otherboxes
"""


def canUnlockAll(boxes):
    """Accepts a list of lists, returns a boolean"""

    keys = []
    unlockable = True

    if len(boxes) < 2:
        return True

    # Collect all valid keys
    for index in range(0, len(boxes)):
        for subIndex in range(0, len(boxes[index])):
            if boxes[index][subIndex] != index:
                keys.append(boxes[index][subIndex])
    keys = list(set(keys))

    # Box 0 is always open
    try:
        keys.remove(0)
    except Exception:
        pass

    # Map boxes to keys
    myMap = {}
    for box in range(1, len(boxes)):
        try:
            myMap[box] = keys[box - 1]
        except Exception:
            myMap[box] = 'X'

    if 'X' in myMap.values():
        unlockable = False
    return unlockable
