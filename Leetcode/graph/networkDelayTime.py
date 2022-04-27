# https://leetcode.com/problems/network-delay-time/
import heapq

def networkDelayTime(times, n, k):
    adj = [[] for _ in range(n + 1)]
    for u, v, w in times:
        adj[u].append((v, w))

    minH = [[0, k]]
    dist = {} # dict of distances from source vertex to every other vertex

    while minH:
        time, node = heapq.heappop(minH)
        if node not in dist:
            dist[node] = time
            for v, w in adj[node]:
                heapq.heappush(minH, [time + w, v])

    return max(dist.values()) if len(dist) == n else -1