# Move zeroes
# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# ==================================================================================================
# Algorithm:
#
# TC: O(n)
# SC: O(1)
# =================================================================================================


# method-1
def move_zeroes(nums):

    if not nums:
        return 0

    n = len(nums)
    count = 0
    i = 0
    while i < n:
        if nums[i] == 0:
            del nums[i]
            count += 1
            n -= 1
            continue

        i += 1

    i = 1
    while i <= count:
        nums.append(0)
        i += 1
    # nums.extend([0]*count)
    return nums


if __name__ == "__main__":

    inputs = [0, 1, 0, 3, 12]  # output: [1,3,12,0,0]
    # inputs = [1]  # output:
    print(move_zeroes(inputs))
