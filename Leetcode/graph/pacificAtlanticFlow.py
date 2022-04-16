# https://leetcode.com/problems/pacific-atlantic-water-flow/

def pacificAtlantic(heights):
    rows, cols = len(heights), len(heights[0])
    pac, atl = set(), set()
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def dfs(r, c, visitSet, prevHeight):
        if ((r, c) in visitSet or 
            r not in range(rows) or
            c not in range(cols) or
            heights[r][c] < prevHeight):
            return
        visitSet.add((r, c))
        for dr, dc in directions:
            dfs(r + dr, c + dc, visitSet, heights[r][c])

    for c in range(cols):
        dfs(0, c, pac, heights[0][c])
        dfs(rows - 1, c, atl, heights[rows - 1][c])
    
    for r in range(rows):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, cols - 1, atl, heights[r][cols - 1])

    res = []
    for r in range(rows):
        for c in range(cols):
            if (r, c) in pac and (r, c) in atl:
                res.append([r, c])

    return res