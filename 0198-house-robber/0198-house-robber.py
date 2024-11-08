class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}
        temp = 0
        ans = float('inf')
        def backtrack(i):
            if i >= len(nums): return 0
            if i in mem: return mem[i]
            include = nums[i] + backtrack(i+2)
            exclude = backtrack(i+1)
            mem[i] = max(include, exclude)
            return mem[i]
        
        backtrack(0)
        return mem[0]