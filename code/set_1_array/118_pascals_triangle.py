# Pascal's Triangle
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
# ======================================================================================
# Algorithm:
#


def generate(num_rows):

    triangle = []

    if not num_rows:
        return triangle

    first_row = [1]
    triangle.append(first_row)

    for i in range(1, num_rows):
        prev_row = triangle[i-1]
        curr_row = list()

        curr_row.append(1)
        for j in range(1, i):
            curr_row.append(prev_row[j-1] + prev_row[j])

        curr_row.append(1)
        triangle.append(curr_row)

    return triangle


if __name__ == "__main__":

    rows_num = 7
    print(generate(rows_num))

# [1],
# [1, 1],
# [1, 2, 1],
# [1, 3, 3, 1],
# [1, 4, 6, 4, 1],
# [1, 5, 10, 10, 5, 1]
