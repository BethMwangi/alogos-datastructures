# Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack with a 
# capacity ‘C.’ The goal is to get the maximum profit out of the knapsack items. Each item can only be 
# selected once, as we don’t have multiple quantities of any item.

# Let’s take Merry’s example, who wants to carry some fruits in the knapsack 
# to get maximum profit. 
# Here are the weights and profits of the fruits:

# Items: { Apple, Orange, Banana, Melon }
# Weights: { 2, 3, 1, 4 }
# Profits: { 4, 5, 3, 7 }
# Knapsack capacity: 5

# Let’s try to put various combinations of fruits in the knapsack, such that their total weight is not more than 5:

# Apple + Orange (total weight 5) => 9 profit
# Apple + Banana (total weight 3) => 7 profit
# Orange + Banana (total weight 4) => 8 profit
# Banana + Melon (total weight 5) => 10 profit

# This shows that Banana + Melon is the best combination as it gives us the maximum profit, 
# and the total weight does not exceed the capacity.


# SOLUTION ONE - RECURSION

def solve_knapsack(profits, weights, capacity):

    return recursive_knapsack(profits, weights, capacity, 0)

def recursive_knapsack(profits, weights, capacity, currentIndex):
    if capacity <= 0 or currentIndex >= len(profits):
        return 0 

    profits1  = 0

    if weights[currentIndex] <= capacity:
        profits1 = profits[currentIndex] + recursive_knapsack(profits, weights, capacity - weights[currentIndex], currentIndex + 1)

    profits2 = recursive_knapsack(profits, weights, capacity, currentIndex + 1)

    return max(profits1, profits2)


def main():
    print(solve_knapsack([1 ,6, 10, 16], [1, 2, 3 ,5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()

# Time and Space complexity#
# The above algorithm’s time complexity is exponential O(2^n)
#  where ‘n’ represents the total number of items. This can also be confirmed from the above recursion tree. As we can see, 
#  we will have a total of ‘31’ recursive calls – calculated through (2^n) + (2^n) - 1
# , which is asymptotically equivalent to O(2^n)


