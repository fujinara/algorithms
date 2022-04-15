# https://leetcode.com/problems/course-schedule/

def canFinish(numCourses, prerequisites):
    g = [[] for _ in range(numCourses)]
    for pair in prerequisites:
        g[pair[1]].append(pair[0])

    color = [0 for _ in range(numCourses)]
    isPossible = True

    def dfs(g, v):
        nonlocal isPossible
        if not isPossible:
            return
        color[v] = 1
        for i in g[v]:
            if color[i] == 0:
                dfs(g, i)
            elif color[i] == 1:
                isPossible = False
        color[v] = 2

    for i in range(numCourses):
        if color[i] == 0:
            dfs(g, i)
    return isPossible