# Summary Ranges
# Given a sorted integer array without duplicates, return the summary of its ranges.

# Example 1:
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

# Example 2:
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
# ==================================================================================================
# Algorithm:
# Using two pointer/iterator
# TC: O(n)
# SC: O(n)
# =================================================================================================


def summary_ranges_1(nums):

    if not nums:
        return []

    summary = []
    left = right = nums[0]

    for i in range(1, len(nums) + 1):

        if i < len(nums) and nums[i] == right + 1:
            right = nums[i]

        else:
            ranges = str(left)
            if left != right:
                ranges += "->" + str(right)
            summary.append(ranges)
            if i < len(nums):
                left = right = nums[i]

    return summary


def summary_ranges(nums):

    if not nums:
        return []

    summary = []
    left = right = 0

    for i in range(1, len(nums) + 1):

        if i < len(nums) and nums[i] == nums[right] + 1:
            right += 1

        else:
            ranges = str(nums[left])
            if left != right:
                ranges += "->" + str(nums[right])
            summary.append(ranges)
            if i < len(nums):
                left = right = i

    return summary


if __name__ == "__main__":

    input_nums = [0, 1, 2, 4, 5, 7]   # Output: ["0->2","4->5","7"]
    # input_nums = [0, 2, 3, 4, 6, 8, 9]   # Output: ["0","2->4","6","8->9"]
    # input_nums = [1]
    print(summary_ranges(input_nums))

