# Longest Consecutive Sequence
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# Your algorithm should run in O(n) complexity.

# Example:
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# ==================================================================================================
# Algorithm:
# Elements of nums are stored in a new set named new_nums
# By definition, set holds unique elements
# While traversing the set, check following conditions for each element --
# 1. If (current element -1) is present in the set, that means the current element
# is already the part of a consecutive sequence. Skip this element or just continue
# 2. If (current element -1) is not present in the set, that means this current element
# can be a start of a consecutive sequence.
# 2-a. Store or update current element in a new variable curr_num  and current length curr_len to 1.
# 2-b. At this point, check if (current element + 1) is present or not in the set.
# If not present, continue. But if present update current length of the sequence.
# 3. When current sequence ends, update longest length sequence = max(longest_len, curr_len)
# 4. Return longest length <-- result
# TC: O(n)
# SC: O(n)
# ==================================================================================================


def longest_consecutive(nums):

    new_nums = set(nums)

    longest_len = 0

    for num in new_nums:
        if num - 1 not in new_nums:
            curr_num = num
            curr_len = 1

            while curr_num + 1 in new_nums:
                curr_len += 1
                curr_num += 1

            longest_len = max(longest_len, curr_len)

    return longest_len


if __name__ == "__main__":

    input_list = [100, 4, 200, 1, 3, 2]  # output: 4
    print(longest_consecutive(input_list))

