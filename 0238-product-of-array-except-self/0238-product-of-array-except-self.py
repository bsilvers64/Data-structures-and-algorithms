class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix, suffix = [1] * (N+1), [1] * (N+1)
        prefix[0], suffix[N] = 1, 1
        for i in range(1, N+1): 
            prefix[i] = prefix[i-1] * nums[i-1]
            suffix[N-i] = suffix[N-i+1] * nums[N-i]
        ans = [1] * (N)
        for i in range(N): ans[i] = prefix[i] * suffix[i+1]
        return ans
