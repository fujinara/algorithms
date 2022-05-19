# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums = set(nums)
        for elem in nums:
            if elem - 1 not in nums:
                cur = 1
                while elem + cur in nums:
                    cur += 1
                ans = max(cur, ans)
        return ans