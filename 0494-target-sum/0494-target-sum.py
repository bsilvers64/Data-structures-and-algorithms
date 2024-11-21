class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, a):
            if (i, a) in memo: return memo[(i, a)]
            if i >= len(nums):
                return 1 if a == target else 0

            memo[(i, a)] = dfs(i+1, a-nums[i]) + dfs(i+1, a+nums[i])
            return memo[(i, a)]
        
        return dfs(0, 0)

