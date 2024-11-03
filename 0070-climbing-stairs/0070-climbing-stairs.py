class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def backtrack(res_sum):
            if res_sum in dp: return dp[res_sum]
            if res_sum > n: return 0
            if res_sum == n: return 1

            dp[res_sum] = backtrack(res_sum+1) + backtrack(res_sum+2)
            return dp[res_sum]

        return backtrack(0)
