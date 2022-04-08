# https://leetcode.com/problems/word-break/

def wordBreak(s, wordDict):
    n = len(s)
    dp = [False for _ in range(n + 1)]
    dp[n] = True
    for i in range(n - 1, -1, -1):
        for w in wordDict:
            if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break
    return dp[0]

s = "dogsandcatcat"
wordDict = ["cats","dog","sand","and","cat","og"]
print(wordBreak(s, wordDict))