# https://leetcode.com/problems/house-robber-ii/

def rob(nums):
    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))

def helper(nums):
    rob1, rob2 = 0, 0
    for elem in nums:
        newRob = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = newRob
    return rob2