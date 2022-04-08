# https://leetcode.com/problems/longest-increasing-subsequence/

def lengthOfLIS(nums):
    n = len(nums)
    LIS = [1 for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
    return max(LIS)