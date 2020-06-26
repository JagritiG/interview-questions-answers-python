# Majority Element II
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# Note: The algorithm should run in linear time and in O(1) space.

# Example 1:
# Input: [3,2,3]
# Output: [3]

# Example 2:
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
# ========================================================================================
# Algorithm:
# TC: O(n)
# SC:

import collections


# Method-1: using collections module
def majority_element(nums):

    if len(nums) == 1:
        return [nums[0]]

    counter = collections.Counter(nums)
    ls = []

    for key in counter:
        if counter[key] > len(nums)//3:
            ls.append(key)

    return ls


# Method-3: Moor's Voting algorithm
# TC: O(n)
# SC: O(1)
def majority_element_(nums):
    pass


if __name__ == "__main__":

    # nums = [3, 2, 3]    # output: [3]
    nums = [1, 1, 1, 3, 3, 2, 2, 2]   # output: [1, 2]
    print(majority_element(nums))
    # print(majority_element_2(nums))
