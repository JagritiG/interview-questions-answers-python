# Combination Sun II
# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.
# Each number in candidates may only be used once in the combination.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.

# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]

# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]
# ==========================================================================


# method-1
def combination_sum2(candidates, target):

    combinations = []
    candidates.sort()

    def find_combinations(target, idx, curr_list):
        if target <= 0:
            if target == 0 and not sorted(curr_list) in combinations:
                combinations.append(sorted(curr_list))
            return

        if idx < len(candidates):
            e = candidates[idx]
            if e > target:
                return
            find_combinations(target-e, idx+1, curr_list+[e])
            find_combinations(target, idx+1, curr_list)

    find_combinations(target, 0, [])
    return combinations


if __name__ == "__main__":
    arr = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    # arr = [2, 5, 2, 1, 2]
    # target = 5
    print(combination_sum2(arr, target))

