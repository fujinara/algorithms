def productExceptSelf(nums):
    n = len(nums)
    pref = 1
    result = [1 for _ in range(n)]
    for i in range(n):
        result[i] = pref
        pref *= nums[i]
    suff = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suff
        suff *= nums[i]
    return result


nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))