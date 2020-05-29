# Two Sum II - Input array is sorted
# Given an array of integers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that
# they add up to the target, where index1 must be less than index2.

# Note:
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and
# you may not use the same element twice.

# Example:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
# ========================================================================
# ToDo: Method-3: Using two iterator i and j for an sorted array
# Time complexity = O(n)
# Space complexity = O(1)


def two_sum(arr, target):

    i = 0
    j = len(arr) - 1
    while i <= j:
        if arr[i] + arr[j] == target:
            return [i+1, j+1]
        elif arr[i] + arr[j] < target:
            i += 1
        else:        # arr[i] + arr[j] > target
            j -= 1
    return []


if __name__ == "__main__":
    a = [2, 7, 11, 15]
    target = 9
    print(two_sum(a, target))
