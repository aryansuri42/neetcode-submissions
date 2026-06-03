class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights)-1
        maxVol = 0
        while start<end:
            vol = min(heights[start], heights[end]) * (end-start)
            maxVol = max(maxVol, vol)
            if heights[start]>heights[end]:
                end-=1
            elif heights[start]<heights[end]:
                start+=1
            else:
                start+=1
        return maxVol