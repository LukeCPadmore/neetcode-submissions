class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMax = 0
        l,r = 0,1
        while r < len(prices):
            currMax = max(currMax, prices[r]-prices[l])
            if prices[l] >= prices[r]:
                l = r
            r+=1

        return currMax