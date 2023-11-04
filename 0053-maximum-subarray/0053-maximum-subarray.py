class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, curr_max, fin_max = nums[0], 0,  float('-inf')
        if len(nums) == 1: return ans
        for i in nums:
            ans = max(i, curr_max + i)
            curr_max = ans
            fin_max = max(ans, fin_max)

        return fin_max