#!/usr/bin/python3
"""Island perimeter
"""


def count_zeros(grid, r, c):
    """Count zeros
    """
    zeros = 0
    # check up
    try:
        if grid[r - 1][c] == 0:
            zeros += 1
    except Exception:
        zeros += 1
    # check down
    try:
        if grid[r + 1][c] == 0:
            zeros += 1
    except Exception:
        zeros += 1
    # check left
    try:
        if grid[r][c - 1] == 0:
            zeros += 1
    except Exception:
        zeros += 1
    # check right
    try:
        if grid[r][c + 1] == 0:
            zeros += 1
    except Exception:
        zeros += 1
    return zeros


def island_perimeter(grid):
    """Find island perimeter
    """
    perimeter = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            # check for 1,
            # if 1, check up, down, left, right for 1 and count ones found.
            # zeros = 4 - ones found
            # sum all zeros found===perimeter
            if grid[r][c] == 1:
                perimeter += count_zeros(grid, r, c)
    return perimeter
