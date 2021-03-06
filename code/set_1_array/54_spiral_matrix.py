# Spiral Matrix
# Given a matrix of m x n elements (m rows, n columns),
# return all elements of the matrix in spiral order.

# Example 1:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# ========================================================


def spiral_order(matrix):

    result = []

    if not matrix or len(matrix) == 0:
        return result

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    size = len(matrix) * len(matrix[0])

    while len(result) < size:

        if top <= bottom:
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1

        if left <= right:
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1

        if top <= bottom:
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


if __name__ == "__main__":

    # nums = [[1, 2, 3],
    #         [4, 5, 6],
    #         [7, 8, 9]]   # Output: [1,2,3,6,9,8,7,4,5]

    # nums = [[1, 2, 3, 4],
    #         [5, 6, 7, 8],
    #         [9, 10, 11, 12]]     # Output: [1,2,3,4,8,12,11,10,9,5,6,7]

    nums = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]     # [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

    print(spiral_order(nums))

