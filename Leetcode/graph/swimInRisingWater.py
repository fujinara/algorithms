# https://leetcode.com/problems/swim-in-rising-water/
from collections import deque
import heapq

def swimInWater(grid):
    n = len(grid)
    minH = [[grid[0][0], 0, 0]] # [maxHeight, r, c]
    visited = set()
    visited.add((0, 0))
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    while minH:
        t, r, c = heapq.heappop(minH)
        if r == n - 1 and c == n - 1:
            return t
        for dr, dc in directions:
            i, j = r + dr, c + dc
            if (i in range(n) and j in range(n) and (i, j) not in visited):
                visited.add((i, j))
                heapq.heappush(minH, [max(t, grid[i][j]), i, j])