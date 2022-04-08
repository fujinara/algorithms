# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
    best = 0
    buy = prices[0]
    for p in prices[1:]:
        if p <= buy:
            buy = p
        else:
            best = max(p - buy, best)
    return best


prices = [7,1,5,3,6,4]
print(maxProfit(prices))