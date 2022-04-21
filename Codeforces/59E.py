from collections import deque

n, m, k = map(int, input().split())
adj = [[] for i in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

banned = set()
for _ in range(k):
    a, b, c = map(int, input().split())
    banned.add((a, b, c))

q = deque()
par = {}
visited = set()

for u in adj[1]:
    q.append((1, u))
    visited.add((1, u))
    par[(1, u)] = [-1, -1]

ans = [-1, -1]
while q:
    x, y = q[0]
    q.popleft()

    if y == n:
        ans = [x, y]
        break

    for z in adj[y]:
        if (x, y, z) in banned:
            continue
        if (y, z) not in visited:
            visited.add((y, z))
            par[(y, z)] = [x, y]
            q.append((y, z))

if ans[0] == -1:
    print(-1)
    exit()

path = []
u, v = ans
path.append(v)
while u != -1:
    path.append(u)
    u, v = par[(u, v)][0], u

print(len(path) - 1)
print(*path[::-1])