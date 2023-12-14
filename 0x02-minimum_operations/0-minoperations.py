#!/usr/bin/python3
""" Defines one function minOperations(n)
"""


def minOperations(n):
    """Calculate the fewest number of operations
        needed to write n H characters given the
        allowed operations WRITE ONE and COPY ALL
    """
    if n <= 1:
        return 0
    for idx in range(2, int(n ** 0.5) + 1):
        if n % 1 == 0:
            return idx + minOperations(n // idx)
    return n
