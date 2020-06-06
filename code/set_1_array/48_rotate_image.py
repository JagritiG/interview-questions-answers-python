# Rotate Image
# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).

# Note: You have to rotate the image in-place, which means you have to modify
# the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:
# Given input matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

# Example 2:
# Given input matrix =
# [
#   [5, 1, 9,11],
#   [2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],
# rotate the input matrix in-place such that it becomes:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]
# ==============================================================================


def rotate_image(matrix):

    # Step-1: Transpose the matrix
    for i in range(len(matrix)):
        # iterate through columns
        for j in range(i, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # print(matrix)

    # Step-2: Flip horizontally
    i = 0
    while i < len(matrix):
        left = 0
        right = len(matrix[i]) - 1
        while left < len(matrix[i])//2:
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1
        i += 1

    return matrix


if __name__ == "__main__":

    # A = [[1, 2],
    #      [3, 4]]
    # # Output: [[3,1],[4,2]]

    # A = [[1, 2, 3],
    #      [4, 5, 6],
    #      [7, 8, 9]]

    # A = [[5, 1, 9, 11],
    #      [2, 4, 8, 10],
    #      [13, 3, 6, 7],
    #      [15, 14, 12, 16]]

    A = [[2, 29, 20, 26, 16, 28],
         [12, 27, 9, 25, 13, 21],
         [32, 33, 32, 2, 28, 14],
         [13, 14, 32, 27, 22, 26],
         [33, 1, 20, 7, 21, 7],
         [4, 24, 1, 6, 32, 34]]
    # Output: [[4,33,13,32,12,2],[24,1,14,33,27,29],[1,20,32,32,9,20],[6,7,27,2,25,26],[32,21,22,28,13,16],[34,7,26,14,21,28]]
    print(rotate_image(A))

# =====================================
# LeetCode:
# Runtime: 24 ms, faster than 98.91% of Python3 online submissions for Rotate Image.
# Memory Usage: 13.7 MB, less than 86.14% of Python3 online submissions for Rotate Image.
