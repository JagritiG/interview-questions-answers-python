# 3Sum Closest
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Example:
# Given array nums = [-1, 2, 1, -4], and target = 1.
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# =============================================================


def three_sum_closest(nums, target):

    # Sort the array:
    nums.sort()       # [-4, -1, 1, 2]

    # calculate sum of first 3 elements of the sorted array
    # sum of [-4, -1, 1] = -4; the reference sum
    expected_sum = sum(nums[:3])

    for i in range(len(nums)-2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            calculated_sum = nums[i] + nums[left] + nums[right]
            if abs(calculated_sum-target) < abs(expected_sum-target):
                expected_sum = calculated_sum
            if calculated_sum < target:
                left += 1
            else:
                right -= 1

    return expected_sum


if __name__ == "__main__":
    a = [-1, 2, 1, -4]
    t = 1
    print(three_sum_closest(a, t))
