"""
print out the idicies of the intervals where we have an increasing sequence of numbers
[0,3,5,2,1,9] -> 0-2,3,4-5
"""

def repr(intervStart, intervEnd):
    if intervStart == intervEnd:
        return str(intervEnd)
    return f'{intervStart}-{intervEnd}'

def getIntervals(nums):
    res = []
    i, j = 0, 0
    while j < len(nums):
        if j == len(nums) - 1 or nums[j + 1] < nums[j]:
            res.append(repr(i, j))
            i, j = j + 1, j + 1
        else:
            j += 1
    return ','.join(res)


nums = [0,3,5,2,1,9]
print(getIntervals(nums))