def threeSum(nums):
    res = []
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == -a:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
            elif nums[l] + nums[r] > -a:
                r -= 1
            else:
                l += 1
    return res


nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))