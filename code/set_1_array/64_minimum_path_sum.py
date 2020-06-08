# Minimum path sum
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right
# which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

# Example:
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# ============================================================
# Algorithm:
# For first row, set grid[0][i] = grid[0][i] + grid[0][i-1] where i <-- 1 to n; because only right move is possible.
# For first column, set grid[j][0] = grid[j][0] + grid[j-1][0] where j <-- 1 to m; because only down move is possible.
# For other locations, there are two options available-> down move and right move.
# To get the minimum sum at location (i, j), add minimum of the previous two options to
# the current element:  grid[i][j] = min(grid[i-1][j], grid[i][j-1]) where i <-- 1 to m, j <-- 1 to n;
# Return grid[m-1][n-1] --> result
# ===================================================================================================================


def min_path_sum(grid):

    m = len(grid)
    n = len(grid[0])

    # fill first row
    for i in range(1, n):
        grid[0][i] += grid[0][i-1]

    # fill first column
    for j in range(1, m):
        grid[j][0] += grid[j-1][0]

    # fill other location
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])

    return grid[m-1][n-1]


if __name__ == "__main__":

    input_grid = [[1, 3, 1],
                     [1, 5, 1],
                     [4, 2, 1]]

    print(min_path_sum(input_grid))
