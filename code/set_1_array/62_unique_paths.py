# Unique Paths
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?

# Example 1:
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right

# Example 2:
# Input: m = 7, n = 3
# Output: 28

# Constraints:
# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
# =========================================================================
# Algorithm:
# Initialize am (m * n) zero matrix
# Set all the elements of the first row and first column as 1: matrix[i][j] =1
# For rows and columns other than first row and first column,
# the element at current position (i, j) is set as:
# matrix[i][j] == matrix[i-1][j] + matrix[i][j-1]
# Finally return the last element at position (m-1, n-1), matrix[m-1][n-1] or matrix[-1][-1]

# _______________________________________________
# | start -> |  1 ->    |  1 ->    |  1         |
# ----|---------|-----------|---------|----------
# | 1 ->     | 1+1=2 -> | 2+1=3 -> | 3+1=4      |
# ----|---------|-----------|---------|----------
# | 1 ->     | 1+2=3 -> | 3+3=6 -> | stop 6+4=10|
# -----------------------------------------------

# Time complexity: O(m * n)
# Space complexity: O(m * n)
# ==========================================================================
import numpy as np


def unique_path(m, n):

    matrix = np.zeros((m, n), dtype=int)

    i = 0
    while i < m:
        j = 0
        while j < n:
            if i == 0 or j == 0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

            j += 1
        i += 1

    # return matrix[m-1][n-1]
    return matrix[-1][-1]


if __name__ == "__main__":

    m = 3
    n = 2
    print(unique_path(m, n))

