class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return nums[0]
        dp0, dp1 = nums[0], max(nums[0], nums[1])
        if N == 2: return dp1

        for i in range(2, N):
            max_so_far = max(nums[i]+dp0, dp1)
            dp0 = dp1
            dp1 = max_so_far
            

        return dp1
        