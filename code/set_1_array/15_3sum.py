# 3Sum
# Given an array nums of n integers, are there elements a, b, c in nums
# such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# Note:
# The solution set must not contain duplicate triplets.

# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4],
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
# =====================================================================


def three_sum(nums):

    nums.sort()
    new_list = []

    for i in range(len(nums)-1):

        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = len(nums) - 1

        while left < right:

            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                new_list.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return new_list


if __name__ == "__main__":
    # a = [-1, 0, 1, 2, -1, -4]
    a = [0, 0, 0]
    # a = [0]
    # a = []
    # a = [-1, 0, -1]
    print(three_sum(a))



