def findMin(nums):
    l = 0
    r = len(nums) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] < nums[l]:
            r = mid
        else:
            l = mid
    return nums[r] if nums[l] > nums[r] else nums[0]

nums = [11,13,15,17]
print(findMin(nums))