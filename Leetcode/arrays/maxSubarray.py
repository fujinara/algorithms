def maxSubArray(nums):
    cur = best = nums[0]
    for elem in nums[1:]:
        cur = max(elem, cur + elem)
        best = max(cur, best)
    return best

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))