# https://leetcode.com/problems/coin-change/

def coinChange(coins, amount):
    dp = [float('inf') for _ in range(amount + 1)]
    dp[0] = 0
    for i in range(amount + 1):
        for c in coins:
            if i - c >= 0 and dp[i - c] != float('inf'):
                dp[i] = min(dp[i], dp[i - c] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


coins = [2]
amount = 3
print(coinChange(coins, amount))