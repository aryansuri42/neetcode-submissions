class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = 0
        e = s+1
        maxdiff = 0

        while s<len(prices)-1:
            while e<len(prices):
                if prices[s]<prices[e]:
                    maxdiff = max(maxdiff, prices[e]-prices[s])
                e+=1
            s+=1
            e=s+1
        return maxdiff            
