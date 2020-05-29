# Combination Sum
# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.
# The same repeated number may be chosen from candidates unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.

# Example 1:
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]

# Example 2:
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
#  =====================================================


# method-1
def combination_sum_1(candidates, target):
    result = []
    candidates.sort()

    def find_combination(current_sum, current_list, target):

        if current_sum == target:
            if not sorted(current_list) in result:
                result.append(sorted(current_list))

        elif current_sum > target:
            return

        for e in candidates:
            if target < e:
                break
            find_combination(current_sum + e, current_list + [e], target)

    find_combination(0, [], target)
    return result


# method-2 (2nd faster) **
def combination_sum_2(candidates, target):

    candidates.sort()
    current_list = []
    result_list = []
    idx = 0

    def find_combination(i, target, current_list):

        if i >= len(candidates):
            return
        for j in range(i, len(candidates)):
            e = candidates[j]
            if e > target:
                break
            elif e == target:
                result_list.append(current_list+[e])
            else:
                find_combination(j, target-e, current_list+[e])
        return

    find_combination(idx, target, current_list)
    return result_list


# method-3 (Faster approach) ***
def combination_sum(candidates, target):

    combinations = []
    candidates.sort()

    def find_combinations(target, idx, curr_list):
        if target <= 0:
            if target == 0:
                combinations.append(sorted(curr_list))
            return

        if idx < len(candidates):
            e = candidates[idx]
            if e > target:
                return
            find_combinations(target-e, idx, curr_list+[e])
            find_combinations(target, idx+1, curr_list)

    find_combinations(target, 0, [])
    return combinations


if __name__ == "__main__":
    # arr = [2, 3, 6, 7]
    # target = 7
    arr = [2, 3, 5]
    target = 8
    # print(combination_sum_1(arr, target))
    # print(combination_sum_2(arr, target))
    print(combination_sum(arr, target))

