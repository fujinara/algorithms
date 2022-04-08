# https://leetcode.com/problems/house-robber/

def rob(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    dp = [0 for _ in range(n)]
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
    return dp[n - 1]

def robBetter(nums):
    rob1, rob2 = 0, 0
    for elem in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2


nums = [1,2,3,1]
print(rob(nums))