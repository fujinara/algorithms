"""
Дан массив из нулей и единиц. Нужно определить, какой максимальный по длине подинтервал единиц можно получить, удалив ровно один элемент массива.
[1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1] -> 5
[1, 1, 1, 1, 1, 1] -> 5
[0, 1, 1, 1, 1] -> 4
[1, 1, 1, 1, 0] -> 4
"""
def func(arr):
    i = j = 0
    n = len(arr)
    s = sum(arr)
    # no zeros
    if s == len(arr):
        return s - 1
    s = 0
    maxinterval = 0
    while j < n:
        while i < n and i - j <= s + 1:
            if arr[i] == 1:  
                s += 1
            i += 1
        maxinterval = max(s, maxinterval)
        if arr[j] == 1:
            s -= 1
        j += 1
    return maxinterval


# def solve(nums):
#     n = len(nums)
#     s = sum(nums)
#     if s == n:
#         return n - 1
#     if s == 0:
#         return 0
#     shrink = []
#     cnt0 = 0
#     cnt1 = 0
#     for i in range(n):
#         if nums[i] == 0:
#             cnt0 -= 1
#             if cnt1 != 0:
#                 shrink.append(cnt1)
#                 cnt1 = 0
#         else:
#             cnt1 += 1
#             if cnt0 != 0:
#                 shrink.append(cnt0)
#                 cnt0 = 0
#         if i == n - 1:
#             if cnt0 != 0:
#                 shrink.append(cnt0)
#             if cnt1 != 0:
#                 shrink.append(cnt1)
#     if len(shrink) == 2:
#         return max(shrink)
#     ans = 0
#     left, mid, right = 0, 1, 2
#     while right < len(shrink):
#         ans = max(ans, shrink[left], shrink[mid], shrink[right])
#         if shrink[mid] == -1:
#             ans = max(ans, shrink[left] + shrink[right])
#         left += 1
#         mid += 1
#         right += 1
#     return ans

nums = [1, 1, 1, 0, 0, 1]
print(solve(nums))
    