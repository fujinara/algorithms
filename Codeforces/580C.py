n, m = map(int, input().split())
cat = list(map(int, input().split()))
cat = [0] + cat
adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = set()
ans = 0

def dfs(v, cnt=0):
    global ans
    cnt = cnt + 1 if cat[v] == 1 else 0
    if cnt > m:
        return
    visited.add(v)
    if len(adj[v]) == 1 and v != 1:
        ans += 1
    for i in adj[v]:
        if i not in visited:
            dfs(i, cnt)

dfs(1)
print(ans)