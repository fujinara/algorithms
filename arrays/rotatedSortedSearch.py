def search(nums, target):
    l = 0
    r = len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid

        # left sorted portion
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        # right sorted portion
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1


nums = [1]
target = 0
print(search(nums, target))