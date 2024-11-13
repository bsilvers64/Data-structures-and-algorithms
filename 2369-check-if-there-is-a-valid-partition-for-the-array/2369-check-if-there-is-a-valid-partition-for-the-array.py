class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        memo = {}

        def backtrack(i):
            if i == len(nums): return True
            if i in memo: return memo[i]

            res = False
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                res = res or backtrack(i+2)
            if i+2 < len(nums) and (
                (nums[i] == nums[i+1] == nums[i+2]) or
                (nums[i] + 1 == nums[i+1] == nums[i+2] - 1)):
                res = res or backtrack(i+3)

            
            memo[i] = res
            return memo[i]
        
        return backtrack(0)