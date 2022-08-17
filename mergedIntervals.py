
# Problem Statement 
# Given a list of intervals, 
# merge all the overlapping intervals to produce a 
# list that has only mutually exclusive intervals.


# Example 1:

# Intervals: [[1,4], [2,5], [7,9]]
# Output: [[1,5], [7,9]]
# Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
# one [1,5].

# Example 2:

# Intervals: [[6,7], [2,4], [5,9]]
# Output: [[2,4], [5,9]]
# Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].


def mergeOverlapIntervals(intervals):

    if len(intervals) < 2:
        return intervals

    sortedIntervals = sorted(intervals, key=lambda x: x[0])

    mergedIntervals = []
    currentIntervals = sortedIntervals[0]
    mergedIntervals.append(currentIntervals)

    for nextIntervals in sortedIntervals:
        _, currentIntervalsEnd = currentIntervals
        nextIntervalsStart, nextIntervalsEnd = nextIntervals


        if currentIntervalsEnd >= nextIntervalsStart:
            currentIntervals[1] = max(currentIntervalsEnd, nextIntervalsEnd)

        else:
            currentIntervals = nextIntervals
            mergedIntervals.append(currentIntervals)
        
    return mergedIntervals


print(mergeOverlapIntervals([[1,4], [2,5], [7,9]]))