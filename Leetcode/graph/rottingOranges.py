# https://leetcode.com/problems/rotting-oranges/
import collections

def orangesRotting(grid):
    m, n = len(grid), len(grid[0])
    # count fresh oranges and add rotten oranges to our queue
    cntFresh = 0
    q = collections.deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                q.append((i, j))
            elif grid[i][j] == 1:
                cntFresh += 1

    # perform bfs starting from rotten oranges
    time = 0
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    while q and cntFresh > 0:
        for _ in range(len(q)):
            r, c = q.popleft()
            for di, dj in directions:
                i, j = r + di, c + dj
                if i in range(m) and j in range(n) and grid[i][j] == 1:
                    grid[i][j] = 2
                    q.append((i, j))
                    cntFresh -= 1
        time += 1

    return time if cntFresh == 0 else -1