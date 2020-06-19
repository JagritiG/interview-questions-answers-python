# Maximal Rectangle
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
# containing only 1's and return its area.

# Example:
# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6
# ===========================================================================
# Algorithm:
# Approach is to consider every row as a histogram and find its largest rectangle
# Create a new list nums = int(matrix[0]); (elements of first row of the matrix after
# converting into integers)
# Consider this nums as a histogram and find its largest rectangle
# Then update elements of nums with the elements of next row of the matrix as follows:
#    nums[i] == 0 if current element of matrix is zero, otherwise
#    nums[i] += current element of matrix
# and find its largest rectangle
# Compute maximal_rectangle = max(current_max_rectangle, maximal_rectangle)
# Continue this up to the length of the matrix
# Return maximal_rectangle <-- result
# ------------------------------------
# Time complexity: O(rows x columns)
# Space complexity: O(columns)
# =================================================================================


def maximal_rectangle(matrix):

    if not matrix:
        return 0

    def largest_rectangle(heights):

        largest_rec = 0
        stack = []
        heights.append('0')

        for i in range(len(heights)):

            while stack and int(heights[i]) < int(heights[stack[-1]]):
                top = stack.pop()
                area = int(heights[top]) * ((i - stack[-1] - 1) if stack else i)
                largest_rec = max(largest_rec, area)

            stack.append(i)

        return largest_rec

    nums = [int(i) for i in matrix[0]]
    maximal_rec = largest_rectangle(nums)

    for i in range(1, len(matrix)):
        for j in range(len(matrix[i])):
            if int(matrix[i][j]) == 0:
                nums[j] = 0
            else:
                nums[j] += int(matrix[i][j])

        curr_area = largest_rectangle(nums)
        maximal_rec = max(curr_area, maximal_rec)

    return maximal_rec


if __name__ == "__main__":
    input_matrix = [["1", "0", "1", "0", "0"],
                    ["1", "0", "1", "1", "1"],
                    ["1", "1", "1", "1", "1"],
                    ["1", "0", "0", "1", "0"]]
    print(maximal_rectangle(input_matrix))
