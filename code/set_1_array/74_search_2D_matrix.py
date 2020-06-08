# Search a 2D matrix
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# Example 1:
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true

# Example 2:
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false
# ===============================================================================================
# Algorithm:
# If target value is greater than the last element of the current row, then continue to next row.
# If target value is less than or equal to the last element of the current row, then traverse this
# row and if found the target return True, else return False.
# ================================================================================================


# method-1
def search_matrix_1(matrix, target):

    if not matrix or len(matrix[0]) == 0:
        return False

    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
            if target <= matrix[i][-1]:
                for j in range(n):
                    if matrix[i][j] == target:
                        return True

    return False


# Method-2
def search_matrix(matrix, target):

    if not matrix or len(matrix[0]) == 0:
        return False

    for i in range(len(matrix)):
            if target > matrix[i][-1]:
                continue
            else:
                if target in matrix[i]:
                    return True

    return False


if __name__ == "__main__":

    # input_matrix = [[1, 3, 5, 7],
    #                 [10, 11, 16, 20],
    #                 [23, 30, 34, 50]]

    # search_target = 3
    # search_target = 13

    # input_matrix = [[]]
    # search_target = 1

    input_matrix = [[1]]
    search_target = 1

    print(search_matrix(input_matrix, search_target))

