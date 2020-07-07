# Product of Array Except Self
# Given an array nums of n integers where n > 1,  return an array output
# such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix
# of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).
# Follow up:
# Could you solve it with constant space complexity?
# (The output array does not count as extra space for the purpose of space complexity analysis.)
# ========================================================================================
# Algorithm:
# TC: O(n)
# SC:
# ========================================================================================


# TC: O(n*n)
# SC: O(1)
def product_except_self_1(nums):

    res = []

    if not nums:
        return res

    for i in range(len(nums)):
        mul = 1
        nums[0], nums[i] = nums[i], nums[0]
        for j in range(1, len(nums)):
            mul *= nums[j]
        res.append(mul)
    return res


# Using division
# TC: O(n)
# SC: O(1)
def product_except_self_2(nums):

    res = []

    if not nums:
        return res

    mul = 1
    for i in range(len(nums)):
        mul *= nums[i]

    for i in range(len(nums)):
        mul = mul//nums[i]
        res.append(mul)

    return res


# Calculating and multiplying left product array and right product array at index i
# TC: O(n)
# SC: O(n)
def product_except_self_3(nums):

    res = []

    if not nums:
        return res

    left = [nums[0]]
    right = [nums[-1]]

    for i in range(1, len(nums)):
        left.append(left[i-1] * nums[i])

    nums.reverse()
    for i in range(1, len(nums)):
        right.append(right[i-1] * nums[i])

    right.reverse()
    for i in range(len(nums)):

        if i == 0:
            res.append(right[i+1])
        if i == len(nums)-1:
            res.append(left[i-1])
        if 0 < i < len(nums)-1:
            res.append(left[i-1] * right[i+1])
    return res


# Calculating and multiplying left product array and rigth product array at index i: inplace
# TC: O(n)
# SC: O(1)
def product_except_self(nums):

    if not nums:
        return []

    res = [nums[0]]
    # Traverse from left and update output array res
    for i in range(1, len(nums)):
        res.append(res[i-1] * nums[i])

    print(res)
    # Traverse from right and update output array res
    product = 1
    for i in range(len(nums)-1, 0, -1):
        res[i] = res[i-1] * product
        product *= nums[i]

    res[0] = product

    return res


if __name__ == "__main__":

    input_list = [1, 2, 3, 4]    # [24, 12, 8, 6]
    print(product_except_self(input_list))

