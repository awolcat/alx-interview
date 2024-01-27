#!/usr/bin/python3
"""Module
"""


def rotate_2d_matrix(matrix):
    """Rotate 2-D matrix by 90 degrees in place
    """
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right

            top_left = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = top_left
        right -= 1
        left += 1
