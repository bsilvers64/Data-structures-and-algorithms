class Solution:
    def fib(self, n: int) -> int:
        dp0, dp1 = 0, 1
        if n == 0: return 0
        for i in range(n-1):
            temp = dp1 + dp0
            dp0 = dp1
            dp1 = temp

        return dp1