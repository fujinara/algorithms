from collections import deque

n, k, d = map(int, input().split())
p = list(map(int, input().split()))
adj = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
q = deque()
needed = set()

for i in range(1, n):
    u, v = map(int, input().split())
    adj[u].append((v, i))
    adj[v].append((u, i))

for st in p:
    q.append(st)
    visited[st] = True

while q:
    v = q.popleft()
    for u, i in adj[v]:
        if not visited[u]:
            visited[u] = True
            q.append(u)
            needed.add(i)

print(n - 1 - len(needed))
for i in range(1, n):
    if i not in needed:
        print(i, end=' ')