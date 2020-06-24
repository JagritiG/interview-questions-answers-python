# Triangle
# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

# Note:
# Bonus point if you are able to do this using only O(n) extra space,
# where n is the total number of rows in the triangle.
# ======================================================================
# Algorithm:
#


def minimum_total(triangle):

    bottom_row = triangle.pop()
    while triangle:
        top_row = triangle.pop()

        for i in range(len(top_row)):
            top_row[i] += min(bottom_row[i], bottom_row[i+1])

        bottom_row = top_row

    return bottom_row[0]


if __name__ == "__main__":

    # input_triangle = [[2],
    #                   [3, 4],
    #                   [6, 5, 7],
    #                   [4, 1, 8, 3]]

    input_triangle = [[-1],
                      [2, 3],
                      [1, -1, -3]]
    print(minimum_total(input_triangle))

