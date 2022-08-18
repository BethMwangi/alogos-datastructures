
# Problem Statement #
# Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

# Example 1:

# Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
# Output: [2, 3], [5, 6], [7, 7]
# Explanation: The output list contains the common intervals between the two lists.
# Example 2:

# Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
# Output: [5, 7], [9, 10]
# Explanation: The output list contains the common intervals between the two lists.




def merge(intervals_a, intervals_b):

    results = []
    
    i, j, start, end = 0, 0, 0, 1

    while i < len(intervals_a) and j < len(intervals_b):

        a_overlaps_b = intervals_a[i][start] < intervals_b[j][start] and \
            intervals_a[i][start] <= intervals_b[j][end]

        b_overlaps_a = intervals_b[j][start] < intervals_a[i][start] and \
            intervals_b[j][start] <= intervals_a[i][end]


        if a_overlaps_b or b_overlaps_a:
            results.append([max(intervals_a[i][start], intervals_b[j][start]), min(intervals_a[i][end], intervals_b[j][end])])

        if intervals_a[i][end] < intervals_b[j][end]:
            i += 1
        else:
            j += 1

    return results

def main():
    print("The intersection is.." + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("The intersection is.." + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))

main()