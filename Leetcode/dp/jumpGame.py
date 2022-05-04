# https://leetcode.com/problems/jump-game/

def canJump(nums: List[int]) -> bool:
    n = len(nums)
    i, maxInd = 0, 0
    while i <= maxInd:
        if maxInd >= n - 1:
            return True
        maxInd = max(maxInd, i + nums[i])
        i += 1
    return False