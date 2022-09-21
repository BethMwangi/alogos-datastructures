# <!-- Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case the sum is 0.

# For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.

# Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1 -->



def maxSubArray(arr):

    curr_max = arr[0]
    curr_min = arr[0]
    max_so_far = arr[0]
    min_so_far= arr[0]

    sum = 0

    for i in range(len(arr)):
        sum += arr[i]


    for i in range(1, len(arr)):
        # Kadane's Algorithm to find Maximum subarray sum.
        curr_max = max(curr_max + arr[i], arr[i])
        max_so_far = max(max_so_far, curr_max)
        # Kadane's Algorithm to find Minimum subarray sum.

        curr_min = min(curr_min + arr[i], arr[i])
        min_so_far = min(min_so_far, curr_min)
        if min_so_far == sum:
            return max_so_far

    return max(max_so_far, sum - min_so_far)

def main():
    print("The max Subarray sum is, " + str(maxSubArray([8, -1, 3, 4])))
    print("The max Subarray sum is, " + str(maxSubArray([11, 10, -20, 5, -3, -5, 8, -13, 10])))
    print("The max Subarray sum is, " + str(maxSubArray([5, -2, 1, -3, 4, -2, 1, -3, 7])))



main()

 
#  Time complexity#
# The time complexity of this solution is linear, O(n)

# Space complexity#
# The space complexity of this solution is constant, O(1)



