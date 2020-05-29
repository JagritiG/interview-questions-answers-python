# Plus One
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list,
# and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# ========================================================

# Time complexity:
# Space complexity:


# Method-1
def plus_one_m1(nums):
    for i in reversed(range(len(nums))):
        if nums[i] < 9:
            nums[i] += 1
            # return nums

        nums[i] = 0
        i -= 1

    nums.extend([1])
    nums[0], nums[-1] = nums[-1], nums[0]

    return nums

    # new_num = [0] * (len(nums)+1)
    # new_num[0] = 1
    # return new_num


# Method-2
def plus_one_m2(nums):
    for i in range(1, len(nums) + 1):
        if nums[-i] != 9:
            nums[-i] += 1
            break
        elif i == len(nums):
            nums.insert(0, 1)
        nums[-i] = 0
    return nums


# Method-3
def plus_one(nums):
        carry = 1
        for i in reversed(range(len(nums))):
            sum = nums[i] + carry
            nums[i] = sum % 10
            carry = sum // 10
        if carry:
            nums.insert(0, carry)
        return nums


if __name__ == "__main__":

    nums = [1, 2, 3]
    # nums = [9, 9, 9, 9]
    # print(plus_one_m1(nums))
    # print(plus_one_m2(nums))
    print(plus_one(nums))
