# Pascal's Triangle
# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
# Note that the row index starts from 0.

# Example:
# Input: 3
# Output: [1,3,3,1]

# Follow up:
# Could you optimize your algorithm to use only O(k) extra space?
# ================================================================
# Algorithm:
#


def get_row(index):

    num_rows = index+1
    triangle = []

    if index > 33:
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

    return triangle[index]


def get_row_2(index):

    num_rows = index+1

    if index > 33:
        return None

    curr_row = [1]

    for i in range(1, num_rows):
        prev_row = curr_row
        curr_row = list()

        curr_row.append(1)
        for j in range(1, i):
            curr_row.append(prev_row[j-1] + prev_row[j])

        curr_row.append(1)

    return curr_row


if __name__ == "__main__":

    row_index = 3
    print(get_row_2(row_index))
