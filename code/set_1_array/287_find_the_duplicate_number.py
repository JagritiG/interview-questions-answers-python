# Find the Duplicate Number
# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
# prove that at least one duplicate number must exist. Assume that there is only one duplicate number,
# find the duplicate one.

# Example 1:
# Input: [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: [3,1,3,4,2]
# Output: 3

# Note:
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.
# =======================================================================================================
# Algorithm:
# Traverse the array --> for each index, perform the following steps:
# 1. at index i of an array nums, if nums[abs(nums[i]) >= 0, make it negative
# 2. at index i of an array nums, if nums[abs(nums[i]) < 0, (negative means the value already encountered),
# return the absolute value of the element at index i --> abs(nums[i]) <-- result
# TC: O(n)
# SC: O(1)
# =======================================================================================================


def find_duplicate(nums):

    for i in range(len(nums)):
        if nums[abs(nums[i])] < 0:
            return abs(nums[i])

        else:
            nums[abs(nums[i])] *= -1


if __name__ == "__main__":

    # inputs = [1, 3, 4, 2, 2]  # output: 2
    inputs = [3, 1, 3, 4, 2]  # output: 3
    print(find_duplicate(inputs))

