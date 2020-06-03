# Rotate Array
# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Follow up:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# Constraints:
# 1 <= nums.length <= 2 * 10^4
# It's guaranteed that nums[i] fits in a 32 bit-signed integer.
# k >= 0
# =============================================================


def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """

    if not nums:
        return 0

    def reverse_list(a, start, end):

        while start < end:
            a[start], a[end] = a[end], a[start]
            start += 1
            end -= 1

    k = k % len(nums)-1
    nums.reverse()
    reverse_list(nums, 0, k)
    reverse_list(nums, k+1, len(nums)-1)

    return nums


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3   # output: [5, 6, 7, 1, 2, 3, 4]
    # arr = [-1, -100, 3, 99]
    # k = 2  # output: [3, 99, -1, -100]
    # arr = [-1]
    # k = 2
    print(rotate(arr, k))

