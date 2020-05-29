# Median of two sorted arrays
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.

# Example 1:
#   nums1 = [1, 3]
#   nums2 = [2]
#   The median is 2.0

# Example 2:
#   nums1 = [1, 2]
#   nums2 = [3, 4]
#   The median is (2 + 3)/2 = 2.5
# ==================================================================================
# Time complexity: O(log (m+n))
# Space complexity:


def find_median_sorted_arrays(nums1, nums2):

    nums1.extend(nums2)
    nums1.sort()
    print(nums1)
    if len(nums1) % 2 == 0:
        mid_1 = int(len(nums1) / 2)
        mid_2 = mid_1 - 1
        median = (nums1[mid_1] + nums1[mid_2]) / 2
    else:
        mid = int(len(nums1) / 2)
        median = nums1[mid]
    return median


if __name__ == "__main__":

    # nums1 = [1, 3]
    # nums2 = [2]
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(find_median_sorted_arrays(nums1, nums2))
