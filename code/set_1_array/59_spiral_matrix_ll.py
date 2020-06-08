# Spiral Matrix II
# Given a positive integer n, generate a square matrix filled with
# elements from 1 to n^2 in spiral order.

# Example:
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
# =================================================
# Algorithm:
# Same as 54_spiral_matrix
import numpy as np


def generate_matrix(n):

    matrix = np.zeros((n, n), dtype=int)
    print(matrix)

    top = 0
    bottom = n - 1
    left = 0
    right = n - 1

    val = 1
    while top <= bottom and left <= right:

        for i in range(left, right+1):
            matrix[top][i] = val
            val += 1
        top += 1

        for i in range(top, bottom+1):
            matrix[i][right] = val
            val += 1
        right -= 1

        for i in range(right, left-1, -1):
            matrix[bottom][i] = val
            val += 1
        bottom -= 1

        for i in range(bottom, top-1, -1):
            matrix[i][left] = val
            val += 1
        left += 1

    return matrix


if __name__ == "__main__":
    num = 3
    print(generate_matrix(num))
