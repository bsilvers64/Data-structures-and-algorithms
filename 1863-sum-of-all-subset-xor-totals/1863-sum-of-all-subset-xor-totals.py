class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, total):
            if len(nums) == i: return total
            return dfs(i+1, nums[i]^total) + dfs(i+1, total)
        
        return dfs(0, 0)