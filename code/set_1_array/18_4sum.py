# 4Sum
# Given an array nums of n integers and an integer target, are there elements a, b, c, and d
# in nums such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.

# Note:
# The solution set must not contain duplicate quadruplets.

# Example:
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
# =============================================================


def four_sum(nums, target):

    nums.sort()
    new_list = []

    for i in range(len(nums)-3):

        if i > 0 and nums[i] == nums[i-1]:
            continue

        for j in range(i+1, len(nums)-2):

            if j > i+1 and nums[j] == nums[j-1]:
                continue

            left = j + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    print([nums[i], nums[j], nums[left], nums[right]])
                    new_list.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < target:
                    left += 1
                else:
                    right -= 1

    return new_list


if __name__ == "__main__":
    # a = [1, 0, -1, 0, -2, 2]
    # a = [-3, -2, -1, 0, 0, 1, 2, 3]
    a = [0, 0, 0, 0]
    t = 0
    print(four_sum(a, t))

