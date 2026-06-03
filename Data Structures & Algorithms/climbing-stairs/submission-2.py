class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        return self.recursive_step(n, dp)

    def recursive_step(self, step, dp):
        if step in dp:
            return dp[step]
        if step == 0:
            return 1
        if step == 1:
            return 1
        
        dp[step] = self.recursive_step(step - 1, dp) + self.recursive_step(step - 2, dp)
        return dp[step]