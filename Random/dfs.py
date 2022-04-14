# simple dfs function
# visited = set()
def simpleDFS(g, v):
    visited.add(v)
    for i in g[v]:
        if i not in visited:
            simpleDFS(g, i)

# dfs with color and timer
# color could be 0 (white), 1 (grey) or 2 (black)
def dfs(g, v):
    timeIn = dfsTimer
    dfsTimer += 1
    color[v] = 1
    for i in g[v]:
        if color[i] == 0:
            dfs(g, i)
    color[v] = 2
    timeOut = dfsTimer
    dfsTimer += 1

# iterative dfs (without recursion)
def dfsIter(g, v):
    stack = []
    stack.append(v)
    while stack:
        u = stack.pop()
        if color[u] == 0:
            color[u] = 1
            stack.append(u)
            for i in g[u]:
                if color[i] == 0:
                    stack.append(i)
        elif color[u] == 1:
            color[u] == 2

# if there are several components in a graph we should launch dfs function multiple times
# until there are no white (unvisited) vertices
def mainDFS(g):
    for i in range(n):
        if color[i] == 0:
            dfs(g, i)