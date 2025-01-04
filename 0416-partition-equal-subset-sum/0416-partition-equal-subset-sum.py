class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        tot = sum(nums)
        target = tot//2

        if tot % 2 != 0: return False

        def dfs(i, total):
            if target == total:
                return True
            if total > target or i >= len(nums):
                return False
            if (i, total) in memo: return memo[(i, total)]
            
            memo[(i, total)] = dfs(i+1, total+nums[i]) or dfs(i+1, total)
            return memo[(i, total)]

        return dfs(0, 0)