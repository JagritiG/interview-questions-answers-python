# Remove duplicates from sorted array II
# Given a sorted array nums, remove the duplicates in-place such that duplicates appeared
# at most twice and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array
# in-place with O(1) extra memory.

# Example 1:
# Given nums = [1,1,1,2,2,3],
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It doesn't matter what you leave beyond the returned length.

# Example 2:
# Given nums = [0,0,1,1,1,1,2,3,3],
# Your function should return length = 7, with the first seven elements of nums being
# modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
# It doesn't matter what values are set beyond the returned length.
# ================================================================================================================


# method
def remove_duplicates_1(nums):

    if not nums:
        return 0

    j = 2
    for i in range(2, len(nums)):
        if nums[j-2] != nums[i]:
            nums[j] = nums[i]
            j += 1

    return j


# method
def remove_duplicates(arr):

    new_index = 2
    for i in range(2, len(arr)):
        if arr[new_index-2] != arr[i]:
            arr[new_index] = arr[i]
            new_index += 1
    return new_index


if __name__ == "__main__":

    arr = [1, 1, 1, 2, 2, 3]
    # print(remove_duplicates_1(arr))
    print(remove_duplicates(arr))
