# Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.

# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# ===========================================================

# Returns the max sum of sub array
# Time complexity: O(n)
# Space complexity: O(1)


# Todo: method-1
def max_sub_array(nums):
    prev_max_sum = curr_max_sum = nums[0]

    for i in nums[1:]:
        prev_max_sum = max(prev_max_sum+i, i)
        curr_max_sum = max(curr_max_sum, prev_max_sum)

    return curr_max_sum


if __name__ == "__main__":

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_sub_array(nums))
    
