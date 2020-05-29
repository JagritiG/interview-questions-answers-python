# Container With Most Water
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
# forms a container, such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.

# Example:
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# =====================================================


# method-1 0(n2)
def max_area_1(height):

    max_area = 0
    for i in range(len(height)-1):
        for j in range(i+1, len(height)):
            wdth = j - i
            ht = min(height[i], height[j])
            curr_area = wdth * ht
            max_area = max(max_area, curr_area)

    return max_area


# method-2: using two iterator (faster approach) *** O(n)
def max_area(height):

    max_ar = 0
    left = 0
    right = len(height) - 1
    while left < right:
        wdth = right - left
        ht = min(height[left], height[right])
        curr_max = ht * wdth
        max_ar = max(max_ar, curr_max)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_ar


if __name__ == "__main__":

    arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # print(max_area_1(arr))
    print(max_area(arr))

