# Next permutation
# Implement next permutation, which rearranges numbers into the lexicographically
# next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible
# order (ie, sorted in ascending order).
# The replacement must be in-place and use only constant extra memory.

# Here are some examples. Inputs are in the left-hand column and
# its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# ===============================================================


def next_permutation(nums):

    # Find the largest i for num[i] < nums[i+1]
    largest_i = -1
    for i in range(len(nums)-1):

        if nums[i] < nums[i+1]:
            largest_i = i

    if largest_i == -1:
        nums.reverse()
        return nums

    # find largest j for nums[j] > nums[largest_i]
    largest_j = -1
    for j in range(len(nums)):
        if nums[largest_i] < nums[j]:
            largest_j = j

    # Swap nums[largest_i] and nums[largest_j]
    nums[largest_i], nums[largest_j] = nums[largest_j], nums[largest_i]

    # Reverse largest_i+1 to len()nums
    end_arr = nums[largest_i+1:len(nums)]
    end_arr.reverse()
    nums[largest_i+1:len(nums)] = end_arr

    return nums


if __name__ == "__main__":
    # arr = [1, 2, 3]  # out: [1,3,2]
    # arr = [3, 2, 1]  # out: [1, 2, 3]
    # arr = [1, 1, 5] # out: [1, 5, 1]
    # arr = [1, 2, 7, 9, 6, 4, 1] # out: [1, 2, 9, 1, 4, 6, 7]
    arr = [1, 7, 9, 9, 8, 3] # out: [1, 8, 3, 7, 9, 9]

    print(next_permutation(arr))
