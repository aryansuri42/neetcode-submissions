class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        start, end = 0, len(height)-1
        maxL, maxR = height[start], height[end]

        while start<end:
            if maxL>maxR:
                end-=1
                maxR = max(maxR, height[end])
                total += maxR - height[end]
            else:
                start+=1
                maxL = max(maxL, height[start])
                total+=maxL - height[start]
        return total
                