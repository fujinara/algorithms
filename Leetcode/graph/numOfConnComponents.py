# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

def countComponents(n, edges):
    g = [[] for i in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    visited = set()

    def dfs(g, v):
        visited.add(v)
        for i in g[v]:
            if i not in visited:
                dfs(g, i)

    cnt = 0
    for i in range(n):
        if i not in visited:
            cnt += 1
            dfs(g, i)
    return cnt


n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(countComponents(n, edges))