# Problem Statement #
# Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

# Example 1:

# Appointments: [[1,4], [2,5], [7,9]]
# Output: false
# Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
# Example 2:

# Appointments: [[6,7], [2,4], [8,12]]
# Output: true
# Explanation: None of the appointments overlap, therefore a person can attend all of them.
# Example 3:

# Appointments: [[4,5], [2,3], [3,6]]
# Output: false
# Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.




# def can_attend_all_appointments(intervals):

#     sortedIntervals = sorted(intervals, key = lambda x: x[0])

#     start, end = 0, 1

#     for i in range(1, len(sortedIntervals)):
#         if sortedIntervals[i][start] < sortedIntervals[i-1][end]:

#             return False
        
#     return True

# def main():
#     print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
#     print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
#     print("Can attend all appointments: " + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


# main()


# Time complexity#
# The time complexity of the above algorithm is O(N*logN)
# O(N∗logN)
# , where ‘N’ is the total number of appointments. Though we are iterating the intervals only once, our algorithm will take O(N * logN)
# O(N∗logN)
#  since we need to sort them in the beginning.

# Space complexity#
# The space complexity of the above algorithm will be O(N)
# O(N)
# , which we need for sorting. For Java, Arrays.sort() uses Timsort, which needs O(N)
# O(N)
#  space.

# Similar Problems#
# Problem 1: Given a list of appointments, find all the conflicting appointments.

# Example:

# Appointments: [[4,5], [2,3], [3,6], [5,7], [7,8]]
# Output: 
# [4,5] and [3,6] conflict. 
# [3,6] and [5,7] conflict.

def conflicting_appointments(intervals):

    start , end = 0, 1
    results = []

    sortedIntervals = sorted(intervals, key = lambda x: x[0])


    for i in range(0, len(sortedIntervals)):
        for j in range(i+1, len(sortedIntervals)):
            if sortedIntervals[j][start] < sortedIntervals[i][end]:
                results.append([sortedIntervals[i], sortedIntervals[j]])


    return results


def main():
    print("Conflicting appointments: " + str(conflicting_appointments([[1, 4], [2, 5], [7, 9]])))
    print("Conflicting appointments: " + str(conflicting_appointments([[6, 7], [2, 4], [8, 12]])))
    print("Conflicting appointments:: " + str(conflicting_appointments([[4, 5], [2, 3], [3, 6]])))
    print("Conflicting appointments:: " + str(conflicting_appointments([[4,5], [2,3], [3,6], [5,7], [7,8]])))


main()
    


