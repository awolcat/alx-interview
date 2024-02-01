#!/usr/bin/python3
"""Making change
"""


def makeChange(coins, total):
    """Fewest coins needed to make total
    """
    count = 0
    index = 0
    if total <= 0:
        return 0
    coins.sort(reverse=True)  # sort descending
    while index < len(coins):
        if coins[index] <= total and total > 0:
            total -= coins[index]
            count += 1
        elif coins[index] > total:
            index += 1
        else:
            break
    if total != 0:
        return -1
    return count
