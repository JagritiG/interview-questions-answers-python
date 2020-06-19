# Largest rectangle in histogram
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the histogram.

# Example:
# Input: [2,1,5,6,2,3]
# Output: 10
# =================================================================================
# Algorithm: Using a stack -- O(n)
# Push the current bar into stack if it is higher than the bar in stack top
# Otherwise, pop all the bars of higher value from the stack
#


def largest_rectangle_area(heights):

    if not heights:
        return 0

    largest_rec = 0
    stack = []
    heights.append(0)

    for i in range(len(heights)):

        while stack and heights[i] < heights[stack[-1]]:
            top = stack.pop()

            if stack:
                area = heights[top] * (i - stack[-1] - 1)
            else:
                area = heights[top] * i
            largest_rec = max(largest_rec, area)

        stack.append(i)

    return largest_rec


if __name__ == "__main__":
    # hist_bar_heights = [2, 1, 5, 6, 2, 3]
    hist_bar_heights = [1, 1]
    # hist_bar_heights = [1]
    print(largest_rectangle_area(hist_bar_heights))
