# Problem Statement #
# Given a list of non-overlapping intervals sorted by their start time,
#  insert a given interval at the correct position and merge all necessary
#  intervals to produce a list that has only mutually exclusive intervals.

# Example 1:

# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
# Output: [[1,3], [4,7], [8,12]]
# Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].
# Example 2:

# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
# Output: [[1,3], [4,12]]
# Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].
# Example 3:

# Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
# Output: [[1,4], [5,7]]
# Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].


from heapq import merge


def insert(intervals, newInterval):

    mergedIntervals = []
    i, start, end = 0, 0, 1

    while i < len(intervals) and intervals[i][end] < newInterval[start]:
        mergedIntervals.append(intervals[i])

        i += 1
    
    while i < len(intervals) and intervals[i][start] <= newInterval[end]:
        newInterval[start] = min(intervals[i][start], newInterval[start])
        newInterval[end] = max(intervals[i][end], newInterval[end])
        i += 1

    mergedIntervals.append(newInterval)

    while i < len(intervals):
        mergedIntervals.append(intervals[i])
        i += 1

    
    return mergedIntervals


def main():
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()


# Time complexity#
# As we are iterating through all the intervals only once, the time complexity of the above algorithm is O(N)
# O(N)
# , where āNā is the total number of intervals.

# Space complexity#
# The space complexity of the above algorithm will be O(N)
# O(N)
#  as we need to return a list containing all the merged intervals.
