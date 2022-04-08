def combinationSum4(nums, target):
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1
    for i in range(1, target + 1):
        for elem in nums:
            if i - elem >= 0:
                dp[i] += dp[i - elem]
    return dp[target]


nums = [9]
target = 3
print(combinationSum4(nums, target))