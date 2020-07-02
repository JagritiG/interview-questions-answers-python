# Contains Duplicate
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.

# Example 1:
# Input: [1,2,3,1]
# Output: true

# Example 2:
# Input: [1,2,3,4]
# Output: false

# Example 3:
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true
# ==================================================================================================
# Algorithm:
# Hashtable
# TC: O(n)
# SC: O(n)
# =================================================================================================


def contains_duplicate(nums):

    if not nums:
        return 0

    ht = dict()
    for i in range(len(nums)):
        if nums[i] in ht:
            return True
        else:
            ht[nums[i]] = nums[i]

    return False


if __name__ == "__main__":

    # input_list = [1, 2, 3, 1]  # output: True
    # input_list = [1, 2, 3, 4]  # output: False
    # input_list = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]  # output: True
    input_list = [3, 3]
    print(contains_duplicate(input_list))

