# Subsets II
# Given a collection of integers that might contain duplicates, nums,
# return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.

# Example:
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
# =====================================================
# Algorithm:
#


def subsets_with_dup(nums):
    subset = []

    def collect_subsets(index, nums, current_set, subset):
        if sorted(current_set) not in subset:
            subset.append(list(sorted(current_set)))
        for i in range(index, len(nums)):
            current_set.append(nums[i])
            collect_subsets(i+1, nums, current_set, subset)
            current_set.pop()

    collect_subsets(0, nums, [], subset)
    return subset


if __name__ == "__main__":

    # input_list = [1, 2, 2]
    # input_list = [4, 4, 4, 1, 4]
    input_list = [4, 1, 0]     # output: [[],[0],[0,1],[0,1,4],[0,4],[1],[1,4],[4]]
    print(subsets_with_dup(input_list))

