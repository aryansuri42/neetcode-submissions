class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dp = {}
        for i in nums:
            if i not in dp:
                dp[i] = 1
            else:
                return True
        return False