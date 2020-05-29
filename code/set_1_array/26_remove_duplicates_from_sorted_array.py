# Remove duplicates from sorted array
# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

# Example:
# Given nums = [0,0,1,1,1,2,2,3,3,4],
# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
# It doesn't matter what values are set beyond the returned length.
#  =============================================================================================

# Returns the number of valid entries after deletion
# Time complexity: O(n)
# Space complexity: O(1)


def remove_duplicates(arr):

    new_index = 1
    for i in range(1, len(arr)):
        if arr[new_index-1] != arr[i]:
            arr[new_index] = arr[i]
            new_index += 1
    print(arr)
    return new_index


def remove_duplicates_2(nums):

    j = 0
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        nums[j] = nums[i]
        j += 1
    return j


if __name__ == "__main__":

    arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # print(remove_duplicates(arr))
    print(remove_duplicates_2(arr))

