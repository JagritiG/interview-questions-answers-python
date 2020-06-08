# Unique paths II
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# Note: m and n will be at most 100.

# Example 1:
# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# ==========================================================================
import numpy as np


# method-1
def unique_path_with_obstacle(obstacle_grid):

    m = len(obstacle_grid)
    n = len(obstacle_grid[0])
    matrix = np.zeros((m, n), dtype=int)

    # fill first row
    for i in range(n):
        if obstacle_grid[0][i] == 1:
            break
        matrix[0][i] = 1

    # fill first column
    for j in range(m):
        if obstacle_grid[j][0] == 1:
            break
        matrix[j][0] = 1

    # fill other location
    for i in range(1, m):
        for j in range(1, n):
            if obstacle_grid[i][j] != 1:
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

    return matrix[m-1][n-1]


if __name__ == "__main__":

    obstacle_grid = [[0, 0, 0],
                     [0, 1, 0],
                     [0, 0, 0]]

    print(unique_path_with_obstacle(obstacle_grid))



