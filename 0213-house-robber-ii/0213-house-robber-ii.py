class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 3: return max(nums)

        def calc(i, n):
            dp0, dp1 = nums[i], max(nums[i], nums[i+1])
            for i in range(i+2, n):
                temp = max(dp1, nums[i]+dp0)
                dp0 = dp1
                dp1 = temp
            return dp1

        return max(calc(0, N-1), calc(1, N))