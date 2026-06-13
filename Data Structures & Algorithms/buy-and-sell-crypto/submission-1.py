class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best = 0
        l = 0
        r = 1
        
        while r < len(prices):
            if prices[r] - prices[l] > best:
                best = prices[r] - prices[l]
                r += 1
            elif prices[r] < prices[l]:
                l = r
                r += 1
            else:
                r += 1

        return best



