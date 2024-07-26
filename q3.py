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
