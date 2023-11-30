#!/usr/bin/python3
"""This module defines pasacal_triangle function"""


def pascal_triangle(n):
    """Create Pascal's triangle:
        params: n: number of rows
        return: list of lists
    """

    triangle = []
    if n <= 0:
        return []
    starter = [1]
    triangle.append(starter)
    for row in range(0, n - 1):
        inner = fill_next_row(triangle[row])
        triangle.append(inner)
    return triangle


def fill_next_row(array):
    """Fill the next row of a pascal triangle
        params: array: last row of triangle
        return: array
    """

    row = []
    if len(array) <= 0:
        return row
    row.append(1)
    for index in range(0, len(array) - 1):
        value = array[index] + array[index + 1]
        row.append(value)
    if len(array) >= 1:
        row.append(1)
    return row
