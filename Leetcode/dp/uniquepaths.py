# https://leetcode.com/problems/unique-paths/

def uniquePaths(m, n):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return dp[m - 1][n - 1]


m = 4
n = 2
print(uniquePaths(m, n))