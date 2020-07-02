# Maximum Product Subarray
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.

# Example 1:
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# =======================================================================
# Algorithm:
# While traversing the integers, keep tracking current maximum and current minimum
# product at index i. If current maximum product is greater than previously set final
# product, then update final product--    final product = current maximum product
# Return final product <-- result
# TC: O(n)
# SC: O(1)


def max_product(nums):

    if not nums:
        return None

    curr_max = curr_min = final_max = nums[0]

    for i in range(1, len(nums)):
        temp = curr_max
        curr_max = max(max(curr_max * nums[i], curr_min * nums[i]), nums[i])
        curr_min = min(min(temp * nums[i], curr_min * nums[i]), nums[i])

        if curr_max > final_max:
            final_max = curr_max

    return final_max


if __name__ == "__main__":

    input_list = [2, 3, -2, 4]  # output: 6
    # input_list = [-2, 0, -1]     # output: 0
    print(max_product(input_list))
