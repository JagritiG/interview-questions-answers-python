# Search Insert Position
# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.
#
# Example 1:
# Input: [1,3,5,6], 5
# Output: 2
# ========================================================================

# Returns the index if target is found
# Time complexity: O(log n)
# Space complexity: O(1)


# Todo: Method-1
def _binary_search(arr, target, left, right):
    if right < left:
        return left

    mid_point = left + (right - left) // 2

    if arr[mid_point] == target:
        return mid_point
    elif arr[mid_point] > target:
        return _binary_search(arr, target, left, mid_point-1)
    else:     # arr[min_point] < target
        return _binary_search(arr, target, mid_point+1, right)


def search_insert_1(arr, target):
    if len(arr) == 0:
            return 0
    if len(arr) == 1:
        if arr[0] >= target:
            return 0
        else:
            return 1
    idx = _binary_search(arr, target, 0, len(arr))
    return idx


# Todo: Method-2
def binary_search(nums, target, left, right):

    mid = left + (right - left) // 2
    if target < nums[mid]:
        binary_search(nums[:mid-1], target, left, mid-1)
    elif target > nums[mid]:
        binary_search(nums[mid+1:], target, mid+1, right)
    else:
        return mid


# Todo: Method-3
def search_insert_2(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target)


if __name__ == "__main__":
    arr = [1, 3, 5, 6]
    target = 5
    print("Index:", search_insert_1(arr, target))
    # print(search_insert_2(arr, target))
    # print(binary_search(arr, target, 0, len(arr)))

