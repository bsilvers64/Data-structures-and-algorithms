class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * N

        dp[0] = nums[0]
        if N == 1: return dp[0]
        dp[1] = max(nums[0], nums[1])
        if N == 2: return dp[1]

        for i in range(2, N):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[-1]