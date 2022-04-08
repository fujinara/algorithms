def climbStairs(n):
    if n == 1:
        return 1
    dp = [0 for _ in range(n)]
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n - 1]

def climbStairs1(n):
    if n == 1:
        return 1
    prev, cur = 1, 2
    for i in range(2, n):
        tmp = cur + prev
        prev = cur
        cur = tmp
    return cur


n = 2
print(climbStairs(n))
print(climbStairs1(n))