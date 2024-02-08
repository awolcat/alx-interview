#!/usr/bin/python3
"""Island perimeter
"""


def count_zeros(grid, r, c):
    """Count zeros
    """
    zeros = 0
    # check up
    if (r != 0):
        if grid[r - 1][c] == 0:
            zeros += 1
    else:
        zeros += 1
    # check down
    if (r < len(grid) - 1):
        if grid[r + 1][c] == 0:
            zeros += 1
    else:
        zeros += 1
    # check left
    if (c != 0):
        if grid[r][c - 1] == 0:
            zeros += 1
    else:
        zeros += 1
    # check right
    if (c < len(grid[r]) - 1):
        if grid[r][c + 1] == 0:
            zeros += 1
    else:
        zeros += 1
    return zeros

def island_perimeter(grid):
    """Find island perimeter
    
    grid is a list of list of integers:
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).
    """
    perimeter = 0
    for r in range(len(grid)):
        for c in range(len(grid)):
            # check for 1,
            # if 1, check up, down, left, right for 1 and count ones found. 
            # zeros = 4 - ones found  
            # sum all zeros found===perimeter
            if grid[r][c] == 1:
                perimeter += count_zeros(grid, r, c)
    return perimeter
