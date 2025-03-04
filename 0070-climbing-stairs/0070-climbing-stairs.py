class Solution:
    def climbStairs(self, n: int) -> int:
        dp1, dp2 = 1, 1
        curr = 1

        while n-1:
            curr = dp1 + dp2
            dp2 = dp1
            dp1 = curr
            n -= 1
        
        return dp1