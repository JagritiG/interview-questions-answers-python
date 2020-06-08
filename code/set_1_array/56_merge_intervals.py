# Merge Intervals
# Given a collection of intervals, merge all overlapping intervals.

# Example 1:
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Example 2:
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# ============================================================================================================
# Algorithm:
# Sort the intervals such that the first element of the beginning interval (current current) is less than
# the first element of the next interval.
# Set current intervals = [first interval] = [first element, last element]
# Append current interval to result = []
# If the first element of the next interval is less than or equal to the last element of the current interval,
# then the intervals overlap.
# Update the last element of current interval to max(current interval[1], next interval[1])
# If the first element of the next interval is greater than the last element of the current interval, then they
# don't overlap. In that case; update current interval = next interval. And append it to the result.
# return result
# =============================================================================================================


def merge(intervals):

    if len(intervals) <= 1:
        return intervals

    intervals.sort()

    result = []
    curr_interval = intervals[0]
    result.append(curr_interval)

    for interval in intervals:
        curr_last = curr_interval[1]
        next_first = interval[0]
        next_last = interval[1]

        if curr_last >= next_first:
            curr_interval[1] = max(curr_last, next_last)
        else:
            curr_interval = interval
            result.append(curr_interval)

    return result


if __name__ == "__main__":

    input_intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # input_intervals = [[2, 6], [1, 3], [15, 18], [8, 10]]
    # input_intervals = [[1, 4], [4, 5]]
    print(merge(input_intervals))
