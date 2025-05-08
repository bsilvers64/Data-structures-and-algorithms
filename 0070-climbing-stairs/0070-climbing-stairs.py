class Solution:
    def climbStairs(self, n: int) -> int:
        dp0, dp1 = 1, 1
        
        for _ in range(n-1):
            temp = dp1 + dp0
            dp0 = dp1
            dp1 = temp
            
        return dp1