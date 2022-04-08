def numDecodings(s: str) -> int:
    n = len(s)
    dp = [0 for _ in range(n + 1)]
    dp[n] = 1
    
    for i in range(n - 1, -1, -1):
        dp[i] = 0 if s[i] == '0' else dp[i + 1]
        if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] in "0123456"):
            dp[i] += dp[i + 2]

    return dp[0]


s = "11106"
print(numDecodings(s))