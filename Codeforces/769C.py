from collections import deque

n, m, k = map(int, input().split())
if k % 2 != 0:
    print("IMPOSSIBLE")
    exit()
grid = [[] for _ in range(n)]
s = None
for r in range(n):
    grid[r] = list(input())
    c = grid[r].find('X')
    if c != -1:
        s = (r, c)

# D L R U
directions = [[1, 0], [0, -1], [0, 1], [-1, 0]]
q = deque()
visited = set()
d = [[None for _ in range(m)] for _ in range(n)] # array of path lengths

q.append(s)
visited.add(s)
d[s[0]][s[1]] = 0

while q:
    v = q.popleft()
    for dr, dc in directions:
        pass