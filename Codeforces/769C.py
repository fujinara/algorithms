from collections import deque

n, m, k = map(int, input().split())
if k % 2 != 0:
    print("IMPOSSIBLE")
    exit()
grid = ['' for _ in range(n)]
sr, sc = -1, -1 # starting row and column
for r in range(n):
    grid[r] = input()
    c = grid[r].find('X')
    if c != -1:
        sr, sc = r, c

# D L R U
directions = {'D' : [1, 0], 'L' : [0, -1], 'R' : [0, 1], 'U' : [-1, 0]}
q = deque()
visited = set()
d = [[None for _ in range(m)] for _ in range(n)] # array of path lengths

q.append((sr, sc))
visited.add((sr, sc))
d[sr][sc] = 0

while q:
    r, c = q.popleft()
    for dr, dc in directions.values():
        i, j = r + dr, c + dc
        if (i in range(n) and
            j in range(m) and
            grid[i][j] == '.' and
            (i, j) not in visited):
            visited.add((i, j))
            q.append((i, j))
            d[i][j] = d[r][c] + 1

ans = []
r, c = sr, sc
for step in range(k):
    for key, val in directions.items():
        i, j = r + val[0], c + val[1]
        if (i in range(n) and
            j in range(m) and
            grid[i][j] != '*' and
            d[i][j] <= k - step):
            r, c = i, j
            ans.append(key)
            break

if len(ans) != k:
    print("IMPOSSIBLE")
else:
    print(''.join(ans))