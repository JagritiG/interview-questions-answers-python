# Contains Duplicate II
# Given an array of integers and an integer k, find out whether there are two distinct
# indices i and j in the array such that nums[i] = nums[j] and the absolute difference
# between i and j is at most k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
# ==================================================================================================
# Algorithm:
# Hashtable
# TC: O(n)
# SC: O(n)
# =================================================================================================


def contains_duplicate(nums, k):

    if not nums:
        return 0

    ht = dict()
    for i in range(len(nums)):
        if nums[i] in ht and i-ht[nums[i]] <= k:
            return True
        else:
            ht[nums[i]] = i
    return False


if __name__ == "__main__":

    # input_list = [1, 2, 3, 1]
    # k = 3   # output: True
    # input_list = [1, 0, 1, 1]
    # k = 1    # output: True
    # input_list = [1, 2, 3, 1, 2, 3]
    # k = 2    # output: False
    # input_list = [-3, -3]
    # k = 1   # True
    input_list = [99, 99]
    k = 2   # True
    print(contains_duplicate(input_list, k))

