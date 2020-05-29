# Remove element
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Example:
# Given nums = [3,2,2,3], val = 3,
# Your function should return length = 2, with the first two elements of nums being 2.
# It doesn't matter what you leave beyond the returned length.
# ==============================================================

# Returns new length
# Time complexity: O(n)
# Space complexity: O(1)


def remove_element_1(nums, target):
    i = 0
    for j in range(len(nums)):
        if nums[j] != target:
            nums[i] = nums[j]
            i += 1
    return i


def remove_element(nums, target):
    j = 0
    for i in range(len(nums)):
        if nums[i] == target:
            continue
        nums[j] = nums[i]
        j += 1
    return j


if __name__ == "__main__":
    arr = [3, 2, 2, 3]
    # arr = [0, 1, 2, 2, 3, 0, 4, 2]
    t = 3
    print(remove_element(arr, t))
    # print(remove_element_1(arr, t))


