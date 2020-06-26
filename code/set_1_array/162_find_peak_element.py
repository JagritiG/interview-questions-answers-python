# Find Peak Element
# A peak element is an element that is greater than its neighbors.
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# You may imagine that nums[-1] = nums[n] = -∞.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5
# Explanation: Your function can return either index number 1 where the peak element is 2,
#              or index number 5 where the peak element is 6.

# Follow up: Your solution should be in logarithmic complexity.
# =========================================================================================
# Algorithm:
# Binary search
# TC: O(logn)
# SC:


# Method-1: iterative method
def find_peak_element(nums):

    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right-left)//2
        if nums[mid] < nums[mid+1]:
            left = mid + 1
        else:
            right = mid

    return left


if __name__ == "__main__":

    nums = [1, 2, 3, 1]     # output: 2
    # nums = [1, 2, 1, 3, 5, 6, 4]   # output: 1 or 5
    # nums = [1]
    # nums = [1, 2]
    # nums = [2, 1]
    print(find_peak_element(nums))

