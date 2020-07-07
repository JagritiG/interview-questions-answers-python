# Combination Sum III
# Find all possible combinations of k numbers that add up to a number n,
# given that only numbers from 1 to 9 can be used and each combination
# should be a unique set of numbers.

# Note:
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.

# Example 1:
# Input: k = 3, n = 7
# Output: [[1,2,4]]

# Example 2:
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
# ==================================================================================================
# Algorithm:
# Backtracking
# TC:
# SC:
# =================================================================================================


def combination_sum3(k, n):

    def helper(n, k, i, curr, result):

        if k == 0:
            if sum(curr) == n:
                result.append(list(curr))
            return

        for j in range(i, 10):
            curr.append(j)
            helper(n, k-1, j+1, curr, result)
            curr.pop()

    result = []
    helper(n, k, 1, [], result)
    return result


if __name__ == "__main__":

    # k, n = 3, 7   # output: [[1, 2, 4]]
    # k, n = 3, 9   # output: [[1,2,6], [1,3,5], [2,3,4]]
    k, n = 3, 15  # [[1,5,9],[1,6,8],[2,4,9],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6]]
    print(combination_sum3(k, n))

