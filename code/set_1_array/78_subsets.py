# Subsets
# Given a set of distinct integers, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.

# Example:
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
# =====================================================================================
# Algorithm:
#
#


def subsets(nums):

    subset = []

    def collect_subsets(index, nums, current_set, subset):
        subset.append(list(current_set))
        for i in range(index, len(nums)):
            current_set.append(nums[i])
            collect_subsets(i+1, nums, current_set, subset)
            current_set.pop()

    collect_subsets(0, nums, [], subset)
    return subset


if __name__ == "__main__":

    input_list = [1, 2, 3]
    print(subsets(input_list))


