class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}
        def robMax(i):
            if i >= len(nums): return 0
            if i in mem: return mem[i]
            mem[i] = max(robMax(i+2)+nums[i], robMax(i+1))
            return mem[i]

        return robMax(0)