class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = float('-inf')
        dp = [1] * len(nums)
        if len(nums) == 1: return 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
            ans = max(ans, dp[i])

        return ans