# Find Minimum in Rotated Sorted Array II
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# Find the minimum element.
# The array may contain duplicates.

# Example 1:
# Input: [1,3,5]
# Output: 1

# Example 2:
# Input: [2,2,2,0,1]
# Output: 0

# Note:
# This is a follow up problem to Find Minimum in Rotated Sorted Array.
# Would allow duplicates affect the run-time complexity? How and why?
# ===================================================================
# Algorithm:
# Binary search
# Two iterator: left and right --> left = 0 and right = len(nums)-1
# If left element or first element is less than right element or last element,
# the numbers array is sorted and smaller element is at index 0
# If first element at index 0 is greater than the last element, then smaller element is
# in between these two elements. Compute mid point and perform modified binary search
# at around mid point
# TC: O(n)
# SC: O(1)
# =====================================================================================


# Method_1
def find_min_1(nums):

    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    left = 0
    right = len(nums) - 1

    while left <= right:

        if nums[left] == nums[right] or nums[left] == nums[left+1]:
            left += 1

        if nums[right] == nums[right-1]:
            right -= 1

        if left >= right or nums[left] < nums[right]:
            return nums[left]

        mid = left + (right-left)//2

        if nums[left] > nums[right]:

            if nums[mid] < nums[right]:
                if nums[mid] < nums[mid-1]:
                    return nums[mid]
                else:  # nums[mid] > nums[mid-1]
                    right = mid

            if nums[mid] > nums[right]:
                if nums[mid+1] < nums[mid]:
                    return nums[mid+1]
                else:  # nums[mid+1] > nums[mid]
                    left = mid + 1


# Method-2
# TC: O(logn)
def find_min(nums):

    if len(nums) == 1 or nums[0] < nums[len(nums)-1]:
        return nums[0]

    left = 0
    right = len(nums) - 1

    if nums[left] == nums[right] or nums[left] == nums[left+1]:
        left += 1

    if nums[right] == nums[right-1]:
        right -= 1

    mid = left + (right-left)//2

    return min(find_min(nums[:mid+1]), find_min(nums[mid+1:]))


if __name__ == "__main__":

    # arr = [3, 3, 1, 1]
    # arr = [1, 1]
    # arr = [3, 1, 1]
    # arr = [1, 3, 5]
    # arr = [3, 1, 3]
    # arr = [3, 3, 1, 3]
    # arr = [2, 2, 2, 0, 1]
    # arr = [10, 1, 10, 10, 10]
    # arr = [10, 10, 10, 1, 10]
    print(find_min(arr))



