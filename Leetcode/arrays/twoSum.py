# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    comp = {}
    for i in range(len(nums)):
        if nums[i] in comp:
            return [comp[nums[i]], i]
        else:
            comp[target - nums[i]] = i
    return -1

nums = [3,2,4]
target = 7
print(twoSum(nums, target))