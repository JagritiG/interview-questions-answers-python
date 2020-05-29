# Trapping Rain water
# Given n non-negative integers representing an elevation map where
# the width of each bar is 1, compute how much water it is able to
# trap after raining.

# Example:
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# =================================


# method-1 (slow)
def trap_water_1(height):

    if not height:
        return 0

    max_left = height[0]
    result = 0
    for i in range(len(height)-1):

        if i > 0:
            max_left = max(max_left, height[i-1])
            max_right = max(height[(i+1):len(height)])
            min_of_two = min(max_left, max_right)
            water = min_of_two - height[i]
            if water > 0:
                result = result + water

    return result


# method-2 (faster) **
def trap_water_2(height):

    left_max = [0]
    right_max = 0
    total_water = 0

    for i in range(1, len(height)-1):
        left_max.append(max(height[i-1], left_max[i-1]))

    for j in range(len(height)-2, -1, -1):
        right_max = max(right_max, height[j+1])
        sum_water = min(right_max, left_max[j]) - height[j]
        if sum_water > 0:
            total_water = total_water + sum_water

    return total_water


# method-3 : two iterator method (faster)***
# Time complexity : O(n)
# Space complexity : O(1)

def trap_water(height):

    level = 0
    left = 0
    right = len(height)-1
    total_water = 0

    while left < right:
        if height[left] < height[right]:
            lower = height[left]
            left += 1
        else:
            lower = height[right]
            right -= 1

        level = max(level, lower)
        total_water += level - lower

    return total_water


if __name__ == "__main__":

    height_arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # height_arr = [0, 2, 0]
    # height_arr = [2, 0, 2]

    # print(trap_water_1(height_arr))
    # print(trap_water_2(height_arr))
    print(trap_water(height_arr))

