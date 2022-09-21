# SOLUTION :
# TOP DOWN USING MEMOIZATION
# Since we have two changing values (capacity and currentIndex) in our recursive 
# function knapsackRecursive(), we can use a two-dimensional array to store the results of all the solved sub-problems.
#  As mentioned above, we need to store results for every sub-array (i.e., for every possible index ‘i’) and every possible capacity ‘c.’



def solve_knapsack(profits, weights, capacity):

    dp = [[-1 for x in range(capacity + 1)] for y in range(len(profits))]

    return recursive_knapsack(dp, profits, weights, capacity, 0)

def recursive_knapsack(dp, profits, weights, capacity, currentIndex):

    #base check

    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    # check if a value has been calculated and memoized in dp

    if dp[currentIndex][capacity] != -1:
        return dp[currentIndex][capacity]

    profits1 = 0

    if weights[currentIndex] <= capacity:
        profits1 = profits[currentIndex] + recursive_knapsack(dp, profits, weights, capacity - weights[currentIndex],currentIndex + 1)

    profits2 = recursive_knapsack(dp, profits, weights, capacity, currentIndex + 1)

    dp[currentIndex][capacity] = max(profits1, profits2)

    return dp[currentIndex][capacity] 


def main():
    print(solve_knapsack([1 ,6, 10, 16], [1, 2, 3 ,5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()


# Time and Space complexity#
# Since our memoization array dp[profits.length][capacity+1] stores the results for all subproblems, we can conclude that we will not have more than N*C
#  subproblems (where ‘N’ is the number of items and ‘C’ is the knapsack capacity). This means that our time complexity will be O(N*C)

# The above algorithm will use O(N*C)
#  space for the memoization array. Other than that, we will use O(N)
#  space for the recursion call-stack. So the total space complexity will be O(N*C + N)
# , which is asymptotically equivalent to O(N*C).
