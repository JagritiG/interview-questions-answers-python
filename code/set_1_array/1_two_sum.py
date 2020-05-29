# Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# ============================================================


# ToDo: Method-1: Brute force for sorted and unsorted array
# Time complexity = O(n^2)
# Space complexity = O(1)

def two_sum_brute_force(arr, target):

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []

# ToDo: Method-2: Hash Table for sorted and unsorted array
# Time complexity = O(n)
# Space complexity = O(n)


# returns the value
def two_sum_hash_table(arr, target):

    ht = dict()
    for i in range(len(arr)):
        if arr[i] in ht:
            return [ht[arr[i]], arr[i]]

        else:
            ht[target - arr[i]] = arr[i]
    return []


# ** returns indices
# using hash table
def two_sum_ht(nums, target):
    ht = dict()
    for i, e1 in enumerate(nums):
        e2 = target - e1
        if e2 not in ht:
            ht[e1] = i
        else:
            return [ht[e2], i]


# ToDo: Method-3: Using two iterator i and j for an sorted array
# Time complexity = O(n)
# Space complexity = O(1)


def two_sum(arr, target):

    i = 0
    j = len(arr)-1
    while i <= j:
        if arr[i] + arr[j] == target:
            return [i, j]
        elif arr[i] + arr[j] < target:
            i += 1
        else:        # arr[i] + arr[j] > target
            j -= 1
    return []


if __name__ == "__main__":
    a = [3, 2, 4]
    target = 6
    # Return the indices
    # print(two_sum_brute_force(a, target))
    print(two_sum_hash_table(a, target))
    # print(two_sum(a, target))
    print("\n")
    print(two_sum_ht(a, target))
