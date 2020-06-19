# Search in rotated sorted array II
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
# You are given a target value to search. If found in the array return true, otherwise return false.

# Example 1:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true

# Example 2:
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false

# Follow up:
# This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
# Would this affect the run-time complexity? How and why?
# =================================================================================================
# Algorithm:
# Modified Binary search
#
# ==============================================================================


def search(nums, target):

    if not nums:
        return False

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right-left) // 2

        if nums[mid] == target:
            return True

        elif nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1

        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:  # elif nums[mid] <= nums[right]
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False


if __name__ == "__main__":
    arr = [2, 5, 6, 0, 0, 1, 2]
    tar = [0, 3, 2, 5, 6, 1]
    # arr = [1]
    # tar = [1, 0]
    for t in tar:
        print(search(arr, t))


