# Search in rotated sorted array
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search.
# If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# ===================================================================


def search(nums, target):

    if target not in nums:
        return -1

    elif len(nums) < 1 and nums[0] == target:
        return 0

    else:
        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            return nums.index(target)


if __name__ == "__main__":
    # arr = [4, 5, 6, 7, 0, 1, 2]
    # t = 0
    # arr = [4, 5, 6, 7, 0, 1, 2]
    # t = 3
    arr = [1, 3]
    t = 3
    print(search(arr, t))

