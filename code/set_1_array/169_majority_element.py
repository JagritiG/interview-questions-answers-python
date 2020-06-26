# Majority Element
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:
# Input: [3,2,3]
# Output: 3

# Example 2:
# Input: [2,2,1,1,1,2,2]
# Output: 2
# ==============================================================================================
# Algorithm:
# TC:
# SC:


# Method-1: Using dictionary
def majority_element_1(nums):

    if len(nums) == 1:
        return nums[0]

    dt = {}
    for i in nums:
        if i not in dt:
            dt[i] = 1
        if dt[i] > len(nums)//2:
            return i
        else:
            dt[i] += 1


# Method-2: By soriting the nums
# TC: O(nlogn + n)
def majority_element_2(nums):

    if len(nums) == 1:
        return nums[0]

    nums.sort()
    # mid_element = nums[len(nums)//2]
    # if nums.count(mid_element) > len(nums)//2:
    #     return mid_element
    return nums[len(nums)//2]


# Method-3: Moor's Voting algorithm
# TC: O(n)

def majority_element(nums):

    # Find the major candidate
    major = 0
    count = 1

    for i in range(len(nums)):
        if nums[major] == nums[i]:
            count += 1
        else:
            count -= 1

        if count == 0:
            major = i
            count = 1

    # Check if this candidate is the major element
    # if nums.count(nums[major]) > len(nums)//2:
    #     return nums[major]
    c = 0
    for i in range(len(nums)):
        if nums[i] == nums[major]:
            c += 1
    if c > len(nums)//2:
        return nums[major]


if __name__ == "__main__":

    # nums = [3, 2, 3]    # output: 3
    nums = [2, 2, 1, 1, 1, 2, 2]   # output: 2
    # print(majority_element_1(nums))
    # print(majority_element_2(nums))
    print(majority_element(nums))
