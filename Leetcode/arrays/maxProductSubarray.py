def maxProduct(nums):
    best = nums[0]
    # curMax/curMmin stores the max/min product of
    # subarray that ends with the current number
    curMin, curMax = 1, 1
    for elem in nums:
        # multiplying by a negative makes big number smaller, small number bigger
        # so we redefine the extremums by swapping them 
        if elem < 0:
            curMax, curMin = curMin, curMax
        # max/min product for the current number is either the current number itself
        # or the max/min by the previous number times the current one
        curMax = max(curMax * elem, elem)
        curMin = min(curMin * elem, elem)
        # the newly computed max value is a candidate for our global result
        best = max(best, curMax)
    return best

nums = [-2,-1,0,-3,-5]
print(maxProduct(nums))