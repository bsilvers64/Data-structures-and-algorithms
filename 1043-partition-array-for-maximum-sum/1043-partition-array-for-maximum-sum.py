class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        memo = {}
        def dfs(i):
            if i in memo: return memo[i]
            if i >= len(arr):
                return 0
            
            curr_max = 0
            res = 0
            for j in range(i, min(i+k, len(arr))):
                curr_max = max(curr_max, arr[j])
                res = max(res, dfs(j+1) + (curr_max * (j-i+1)))
            
            memo[i] = res
            return res


        return dfs(0)