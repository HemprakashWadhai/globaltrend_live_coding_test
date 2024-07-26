# Write a function to find the longest common subsequence of two given strings. Sample Test Case Input: str1 = "abcde", str2 = "ace" Output: 3 (The LCS is "ace")

def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

str1 = "abcde"
str2 = "ace"
print(longest_common_subsequence(str1, str2))  
