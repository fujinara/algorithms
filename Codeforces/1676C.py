def diff(a, b, m):
    res = 0
    for i in range(m):
        res += abs(ord(a[i]) - ord(b[i]))
    return res

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = []
    ans = float('inf')
    for _ in range(n):
        s.append(input())
    for i in range(n):
        for j in range(i + 1, n):
            ans = min(ans, diff(s[i], s[j], m))
    print(ans)