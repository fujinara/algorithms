def solve():
    n = int(input())
    a = set(map(int, input().split()))
    if n & 1 == len(a) & 1:
        print(len(a))
    else:
        print(len(a) - 1)


t = int(input())
for _ in range(t):
    solve()