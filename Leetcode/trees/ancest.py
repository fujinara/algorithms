# determine if node "a" is an ancestor of node "b" in a tree

n = int(input())
arr = list(map(int, input().split()))

tree = [[] for _ in range(n + 1)]
root = None
for idx, elem in enumerate(arr):
    if elem == 0:
        root = idx + 1
    else:
        tree[elem].append(idx + 1)
    
timerIn = [0] * (n + 1)
timerOut = [0] * (n + 1)
used = set()
dfsTimer = 0

def dfs(v):
    global dfsTimer
    timerIn[v] = dfsTimer
    dfsTimer += 1
    used.add(v)
    for i in tree[v]:
        if i not in used:
            dfs(i)
    timerOut[v] = dfsTimer
    dfsTimer += 1

dfs(root)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    if timerOut[a] > timerOut[b] and timerIn[a] < timerIn[b]:
        print(1)
    else:
        print(0)