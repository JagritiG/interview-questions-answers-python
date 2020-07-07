# Missing Number
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
# find the one that is missing from the array.

# Example 1:
# Input: [3,0,1]
# Output: 2

# Example 2:
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# Note:
# Your algorithm should run in linear runtime complexity.
# Could you implement it using only constant extra space complexity?
# ==================================================================================================
# Algorithm:
# 1. Using hashtable
# TC: O(n)
# SC: O(n)
# 2. Applying Gauss's law : sum of series (1, 2, 3,...,n) = (n/2)*(n+1)
# and with some no skipping: sum of series (1, 4, 7,...,n) = (n/2)*(first element + last element)
# last element = first element + (n-1)d, where d = distance between two elements
# TC: O(n)
# SC: O(1)
# =================================================================================================


# 1. Using hashtable
def missing_number_ht(nums):

    ht = set(nums)

    for i in range(len(nums)+1):
        if i not in ht:
            return i
    return -1


# 2. Applying Gauss's law
def missing_number_gl(nums):

    nums_sum = 0
    n = len(nums)
    for i in nums:
        nums_sum += i

    missing_no = n*(n+1)//2 - nums_sum
    return missing_no


# 3. Applying Gauss's law
def missing_number(nums):

    # n = len(nums)
    # missing_no = n*(n+1)//2 - sum(nums)
    # return missing_no
    return len(nums)*(len(nums)+1)//2 - sum(nums)


if __name__ == "__main__":

    inputs = [3, 0, 1]   # output: 2
    # inputs = [9, 6, 4, 2, 3, 5, 7, 0, 1]   # output: 8
    # inputs = [1]   # outputs: 0
    # inputs = [0]  # outputs: 1
    # print(missing_number_ht(inputs))
    # print(missing_number_gl(inputs))
    print(missing_number(inputs))

