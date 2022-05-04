# https://leetcode.com/problems/cheapest-flights-within-k-stops/

def findCheapestPrice(n, flights, src, dst, k):
    prices = [float('inf') for _ in range(n)]
    prices[src] = 0
    
    for _ in range(k + 1):
        tmpPrices = prices.copy()
        for s, d, p in flights:
            if prices[s] != float('inf'):
                tmpPrices[d] = min(tmpPrices[d], prices[s] + p)
        prices = tmpPrices

    return prices[dst] if prices[dst] != float('inf') else -1