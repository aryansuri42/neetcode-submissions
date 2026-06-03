class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high
        while low<=high:
            mid = (high + low) // 2
            totaltime = 0
            for pile in piles:
                totaltime+=math.ceil(pile/mid)
            if totaltime <= h:
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1

        return res
