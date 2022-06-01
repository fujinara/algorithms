"""
[1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
[1,4,3,2] => "1-4"
[1,4] => "1,4"
"""

def repr(intervStart, intervEnd):
    if intervStart == intervEnd:
        return str(intervEnd)
    return f'{intervStart}-{intervEnd}'

def collapse(nums):
    res = []
    nums.sort()
    i, j = 0, 0
    while j < len(nums):
        if j == len(nums) - 1 or nums[j + 1] - nums[j] > 1:
            res.append(repr(nums[i], nums[j]))
            i, j = j + 1, j + 1
        else:
            j += 1
    return ','.join(res)

nums = [1,4,5,2,3,9,8,11,0]
print(collapse(nums))