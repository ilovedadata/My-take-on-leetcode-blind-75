class Solution(object):
    def maxProfit(self, prices:list[int]) -> int:
        l, r = 0,1 
        max_pr = 0
        while r < len(prices):
            if prices[l] < prices[r]: 
                profit = prices[r] - prices[l]
                if profit > max_pr:
                    max_pr = profit
            else:
                l = r
            r = r + 1
        return max_pr