# https://leetcode.com/problems/course-schedule/

def canFinish(numCourses, prerequisites):
    g = [[] for _ in range(numCourses)]
    for pair in prerequisites:
        g[pair[1]].append(pair[0])

    color = [0 for _ in range(numCourses)]

    def dfs(g, v):
        color[v] = 1
        for i in g[v]:
            if color[i] == 0:
                if not dfs(g, i):
                    return False
            elif color[i] == 1:
                return False
        color[v] = 2
        return True

    for i in range(numCourses):
        if not dfs(g, i):
            return False
    return True