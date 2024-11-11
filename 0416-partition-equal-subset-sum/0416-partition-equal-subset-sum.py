class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1: return False
        s //= 2

        mem = {}
        def dfs(i, total):
            if (i, total) in mem: return mem[(i, total)]
            if i >= len(nums):
                return total == s
            
            mem[(i, total)] = dfs(i+1, total+nums[i]) or dfs(i+1, total)
            return mem[(i, total)]
        
        return dfs(0, 0)