# Insert interval
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.

# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
# ================================================================================
# Algorithm
# Append the new_interval and sort the intervals
# Set current intervals = [first interval] = [first element, last element]
# Append current interval to result = []
# If the first element of the next interval is less than or equal to the last element of the current interval,
# then the intervals overlap.
# Update the last element of current interval to max(current interval[1], next interval[1])
# If the first element of the next interval is greater than the last element of the current interval, then they
# don't overlap. In that case; update current interval = next interval. And append it to the result.
# return result
# =============================================================================================================


def insert(intervals, new_interval):

    if len(intervals) < 1:
        intervals.append(new_interval)
        return new_interval

    intervals.append(new_interval)
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

    # input_intervals = [[1, 3], [6, 9]]
    # new = [2, 5]
    input_intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    new = [4, 8]
    print(insert(input_intervals, new))
