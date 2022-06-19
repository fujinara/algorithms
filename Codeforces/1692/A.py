def solve():
    a, b, c, d = map(int, input().split())
    cnt = 0
    for i in [b, c, d]:
        if i > a:
            cnt += 1
    print(cnt)

t = int(input())
for _ in range(t):
    solve()
