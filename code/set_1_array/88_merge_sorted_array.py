# Merge Sorted Array
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n)
# to hold additional elements from nums2.

# Example:
# Input:
#   nums1 = [1,2,3,0,0,0], m = 3
#   nums2 = [2,5,6],       n = 3
# Output: [1,2,2,3,5,6]
# ========================================================

# Time complexity:
# Space complexity:
# None Do not return anything, modify nums1 in-place instead


def marge_sorted_array(nums1, m, nums2, n):

    nums1[m:m+n] = nums2
    nums1.sort()

    return nums1


if __name__ == "__main__":

    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    n = len(nums2)
    m = len(nums1) - n
    print(marge_sorted_array(nums1, m, nums2, n))
