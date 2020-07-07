# Find All Duplicates in an Array
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements that appear twice in this array.
# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]
# Output:
# [2,3]
# ==================================================================================================
# Algorithm:
# Traverse the array --> for each index, perform the following steps:
# 1. at index i of an array nums, if nums[abs(nums[i]) >= 0, make it negative
# 2. at index i of an array nums, if nums[abs(nums[i]) < 0, (negative means the value already encountered),
# return the absolute value of the element at index i --> abs(nums[i]) <-- result
# TC: O(n)
# SC: O(1)
# ==================================================================================================


# Method-1 using hashtable
# TC: O(n)
# SC: O(n)
def find_duplicates_1(nums):

    res = []
    ht = dict()
    for i in range(len(nums)):
        if nums[i] in ht:
            res.append(nums[i])
        else:
            ht[nums[i]] = nums[i]
    return res


# Method-2
# TC: O(n)
# Without extra space
def find_duplicates(nums):

    res = []
    for i in range(len(nums)):
        if nums[abs(nums[i])-1] < 0:
            res.append(abs(nums[i]))

        else:
            nums[abs(nums[i])-1] *= -1

    return res


if __name__ == "__main__":

    inputs = [4, 3, 2, 7, 8, 2, 3, 1]  # output: [2, 3]
    print(find_duplicates(inputs))


