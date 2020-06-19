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
# Algorithm:
# Modified Binary search
# Find index of smallest element
# If target is greater than the smallest element and less than the last element,
# perform binary search on right part of the array; else perform binary search
# on left part of the array
# ==============================================================================


# Method-1 (faster) ***
def search(nums, target):

    if not nums:
        return -1

    # Find index of smallest element
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right-left)//2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    # If target is greater than the smallest element and less than the last element,
    # perform binary search on right part of the array; else perform binary search
    # on left part of the array
    temp = left     # index of smallest element
    left = 0
    right = len(nums) - 1

    if nums[temp] <= target <= nums[right]:
        left = temp
    else:
        right = temp

    # Perform binary search
    while left <= right:
        mid = left + (right-left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Method-2
def search_2(nums, target):

    if not nums:
        return -1

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2]
    t = 0
    # arr = [4, 5, 6, 7, 0, 1, 2]
    # t = 3
    # arr = [1, 3]
    # t = 3
    # print(search_1(arr, t))
    print(search(arr, t))

