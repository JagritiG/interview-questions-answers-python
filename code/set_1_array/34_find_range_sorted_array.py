# Find first and last position of element in sorted array
# Given an array of integers nums sorted in ascending order,
# find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# ==============================================================


# method-1
def search_range_1(nums, target):
        if target not in nums:
            return [-1, -1]

        elif len(nums) == 1 and nums[0] == target:
            return [0, 0]

        else:
            res = []
            for i in range(len(nums)):
                if nums[i] == target:
                    res.append(i)
            return [res[0], res[-1]]


# method-2 (faster) ***
def search_range(nums, target):

    if target not in nums:
        return [-1, -1]

    elif len(nums) > 1:
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)

        return [res[0], res[-1]]

    else:
        return [0, 0]


if __name__ == "__main__":
    arr = [5, 7, 7, 8, 8, 10]
    t = 8
    # arr = [5, 7, 7, 8, 8, 10]
    # t = 6
    # arr = [1, 1]
    # t = 1
    # arr = [1]
    # t = 1
    # print(search_range_1(arr, t))
    print(search_range(arr, t))

