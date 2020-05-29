# First Missing Positive
# Given an unsorted integer array, find the smallest missing positive integer.

# Note:
# Your algorithm should run in O(n) time and uses constant extra space.


# Example 1:
# Input: [1,2,0]
# Output: 3

# Example 2:
# Input: [3,4,-1,1]
# Output: 2

# Example 3:
# Input: [7,8,9,11,12]
# Output: 1
# ===================================================================

# Returns first missing positive (Faster approach) ***
def first_missing_positive(nums):

    if nums:
        max_val = max(nums)
        if max_val <= 0:
            return 1

        for e in range(1, max_val+1):
            if e not in nums:
                return e
        return max_val+1
    else:
        return 1


if __name__ == "__main__":
    arr = [1, 2, 0] # out: 3
    # arr = [3, 4, -1, 1] # out: 2
    # arr = [7, 8, 9, 11, 12] # out: 1
    # arr = [2]
    print(first_missing_positive(arr))


