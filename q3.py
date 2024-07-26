# Write a function to solve the 0/1 Knapsack problem using dynamic programming.
# Sample Test Case
# Input: weights = [1, 2, 3], values = [10, 15, 40], capacity = 6 Output: 55 (Maximum value that can be obtained)
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]

weights = [1, 2, 3]
values = [10, 15, 40]
capacity = 6
print(knapsack(weights, values, capacity))  
