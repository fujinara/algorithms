def maxArea(height):
    l = 0
    r = len(height) - 1
    best = 0
    while l < r:
        best = max(best, (r - l) * min(height[l], height[r]))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return best


height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))