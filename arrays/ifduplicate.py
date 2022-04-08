def ifDuplicate(nums):
    return len(set(nums)) != len(nums)

def ifDuplicate2(nums):
    elems = set()
    for i in nums:
        if i in elems:
            return True
        else:
            elems.add(i)
    return False

nums = [1,2,3,1]
print(ifDuplicate2(nums))