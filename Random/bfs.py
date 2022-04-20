# adj - adjacency list
# n - number of nodes
# s - source vertex
from collections import deque

adj = [[1, 3, 5], [0, 2], [1, 7], [0, 4, 7], [3], [0, 6, 7], [5, 7], [2, 3, 5, 6]]
n = len(adj)
q = deque()
visited = set()
d = [None for i in range(n)] # array of path lengths
p = [None for i in range(n)] # array of parents

def bfs(adj, s):
    q.append(s)
    visited.add(s)
    p[s] = -1
    d[s] = 0
    while q:
        v = q.popleft()
        for u in adj[v]:
            if u not in visited:
                visited.add(u)
                q.append(u)
                d[u] = d[v] + 1
                p[u] = v

# shortest path from s to u
def shortestPath(adj, s, u):
    bfs(adj, s)
    if u not in visited:
        print("No path!")
    else:
        path = []
        v = u
        while v != -1:
            path.append(v)
            v = p[v]
        path.reverse()
        print("Path: ", end='')
        for v in path:
            print(v, end=' ')
        print()
        print(f'Length: {d[u]}')

shortestPath(adj, 5, 4)
