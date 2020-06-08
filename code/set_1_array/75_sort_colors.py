# Sort colors
# Given an array with n objects colored red, white or blue, sort them in-place so that
# objects of the same color are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# Note: You are not suppose to use the library's sort function for this problem.

# Example:
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array
# with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?
# ======================================================================================================================
# Algorithm (one pass): O(1) space complexity
# Initiate three pointer : left -> first index , right -> last index, and curr -> first index
# If element at current index nums[curr] is equal to 0, swap it with element at index left; swap(nums[curr], nums[left])
# Increment left and curr by 1; left += 1, curr += 1
# If element at current index nums[curr] is equal to 2, swap it with element at index right; swap(nums[curr], nums[right])
# Decrement right by 1; right -= 1. Note: we don't increment curr, because
# we din't see the right element (it can be 0 or 1 or 2) which need to be moved to its proper location.
# Else, continue
# Return nums <-- result
# ======================================================================================================================


# Method-1
def sort_colors(nums):

    if not nums or len(nums) == 1:
        return

    left = 0
    right = len(nums) - 1
    curr = 0

    while curr <= right and left < right:
        if nums[curr] == 0:
            nums[left], nums[curr] = nums[curr], nums[left]
            curr += 1
            left += 1

        elif nums[curr] == 2:
            nums[right], nums[curr] = nums[curr], nums[right]
            right -= 1

        else:
            curr += 1

    return nums


# Method-2 using quicksort
def sort_colors_qs(nums):

    def partition(nums, lo, hi):
        pivot = nums[hi]
        i = lo
        for j in range(lo, hi):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[hi] = nums[hi], nums[i]
        return i

    def quick_sort(nums, lo, hi):
        if lo < hi:
            p = partition(nums, lo, hi)
            quick_sort(nums, lo, p-1)
            quick_sort(nums, p+1, hi)

    quick_sort(nums, 0, len(nums)-1)
    return nums


if __name__ == "__main__":

    color_list = [2, 0, 2, 1, 1, 0]
    print(sort_colors(color_list))
    # print(sort_colors_qs(color_list))
