# Jump Game II
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.

# Example:
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Note: You can assume that you can always reach the last index.
# =============================================================


# method-1
def min_jump(nums):

    if not nums:
        return False

    if nums[0] == 0:
        return False

    jump_arr = [-1] * len(nums)
    jump_arr[len(nums)-1] = 0
    for i in range(len(nums)-2, -1, -1):
        if i + nums[i] >= len(nums)-1:
            jump_arr[i] = 1
        else:
            jump_arr[i] = 1 + min(jump_arr[i+1:min(i+nums[i]+1, len(nums)-1)])
    return jump_arr[0]


# method-2 O(n)
def jump_2(nums):

    size = len(nums)

    # destination is last index
    destination = size - 1

    # record of current coverage, record of last jump index
    cur_coverage, last_jump_index = 0, 0

    # counter for jump
    times_of_jump = 0

    # Quick response if start index == destination index == 0
    if size == 1:
        return 0

    # Greedy strategy: extend coverage as long as possible with lazy jump
    for i in range( 0, size):

        # extend current coverage as further as possible
        cur_coverage = max( cur_coverage, i + nums[i] )

        # forced to jump (by lazy jump) to extend coverage
        if i == last_jump_index:

            # update last jump index
            last_jump_index = cur_coverage

            # update counter of jump by +1
            times_of_jump += 1

            # check if reached destination already
            if cur_coverage >= destination:
                    return times_of_jump

    return times_of_jump


# method-3 Greedy O(n)
def jump_3(nums):

    if len(nums) < 2:
        return 0

    cur = front = 0
    steps = 0

    for i in range(len(nums)):
        if i + nums[i] >= len(nums)-1:
            steps += 1
            break

        if i + nums[i] > front:
            front = i+nums[i]

        if i >= cur:
            steps += 1
            cur = front

    return steps


# method-4 O(n), O(1)
def jump_4(nums):

    size = len(nums)
    if size <= 1:
        return 0

    count = nums[0]
    k = 1
    maximum = 1

    for i in range(1,size,1):
        if i <= count:
            maximum = max(maximum,nums[i] + i)
        else:
            k += 1
            count = maximum
            maximum = nums[i] + i

    return k


# Method--5 (faster) ****
# O(n), O(1)
def jump(nums):

    if not nums:
        return False

    if len(nums) == 0 or len(nums) == 1:
        return 0

    max_jump_length = nums[0]
    next_jump_length = nums[0]
    jump_count = 1

    for i in range(1, len(nums)-1):

        # if (i + nums[i]) > next_jump_length:
        #     next_jump_length = i + nums[i]
        next_jump_length = max(next_jump_length, i+nums[i])

        if max_jump_length == i and i != len(nums)-1:
            max_jump_length = next_jump_length
            jump_count += 1

        if max_jump_length >= len(nums)-1:
            break

    return jump_count


if __name__ == "__main__":

    nums = [2, 3, 1, 1, 4]  # 2
    # nums = []
    # nums = [0]
    # nums = [1]
    # nums = [0, 2]
    # nums = [2, 0]
    # nums = [2, 1]
    # nums = [1, 2, 1, 1, 1]  # 3
    # print(min_jump(nums))
    # print(jump_2(nums))
    # print(jump_3(nums))
    # print(jump_4(nums))
    print(jump(nums))
