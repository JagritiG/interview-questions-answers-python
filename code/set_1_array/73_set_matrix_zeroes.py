# Set matrix zeroes
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

# Example 1:
# Input:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]

# Example 2:
# Input:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]

# Follow up:
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
# =====================================================================================
# Algorithm:
# Initialize a default value which is not present in the given input matrix.
# While walk through the matrix, if element at position (i, j),i.e., matrix[i][j] is 0,
# set all the non-zero element in the row i and in the column j as default value.
# Finally set all the element equal to default value as 0 <-- result
# ======================================================================================


def set_zeroes(matrix):

    if not matrix:
        return 0

    m = len(matrix)
    n = len(matrix[0])
    default_value = max(map(max, matrix)) + 1

    for i in range(m):
        for j in range(n):

            if matrix[i][j] == 0:
                # Set row to default value
                for col in range(n):
                    if matrix[i][col] != 0:
                        matrix[i][col] = default_value

                # Set column to default value
                for row in range(m):
                    if matrix[row][j] != 0:
                        matrix[row][j] = default_value

    # print(matrix)
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == default_value:
                matrix[i][j] = 0

    return matrix


if __name__ == "__main__":

    # input_matrix = [[1, 1, 1],
    #                 [1, 0, 1],
    #                 [1, 1, 1]]

    input_matrix = [[0, 1, 2, 0],
                    [3, 4, 5, 2],
                    [1, 3, 1, 5]]
    print(set_zeroes(input_matrix))
