# https://leetcode.com/problems/reconstruct-itinerary/

def findItinerary(tickets):
    g = {u : collections.deque() for u, v in tickets}
    res = ["JFK"]
    
    tickets.sort()
    for u, v in tickets:
        g[u].append(v)
    
    def dfs(cur):
        if len(res) == len(tickets) + 1:
            return True
        if cur not in g:
            return False
        
        temp = list(g[cur])
        for v in temp:
            g[cur].popleft()
            res.append(v)
            if dfs(v):
                return res
            res.pop()
            g[cur].append(v)
        return False

    dfs("JFK")
    return res