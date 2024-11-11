class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans, pref, suff = float('-inf'), 1, 1
        N = len(nums)

        for i in range(N):
            pref *= nums[i]
            suff *= nums[N-i-1]
            ans = max(ans, pref, suff)
            if pref == 0: pref = 1 
            if suff == 0: suff = 1

        return ans