# Minimum Size Subarray Sum
# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Example:
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.

# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
# ==================================================================================================
# Algorithm:
# Set minimal length to the (length of the array + 1)
# Set pointer start to index 0
# Set current sum curr_sum = 0
# While traversing the array, calculate current sum up to index i.
# Check if current sum curr_sum is greater than or equal to the target sum;
# update minimal length as: min_len = min(min_len, i+1-start).
# Pop the start element of this current series and increment start pointer by 1
# Repeat the above steps till the end.
# If minimal length is found other than the (length of the array + 1),
# return minimal length, else return 0 <-- result
# =================================================================================================
# TC: O(n)
# SC: O(1)
# =================================================================================================


def min_sub_array_len(nums, s):

    min_len = len(nums) + 1
    start = 0
    curr_sum = 0

    for i in range(len(nums)):
        curr_sum += nums[i]

        while curr_sum >= s:
            min_len = min(min_len, i+1-start)
            curr_sum -= nums[start]       # pop the start element of the series
            start += 1                    # increment start pointer by 1

    if min_len is not len(nums) + 1:
        return min_len
    else:
        return 0


if __name__ == "__main__":

    s = 7
    input_list = [2, 3, 1, 2, 4, 3]  # output: 2
    print(min_sub_array_len(input_list, s))

