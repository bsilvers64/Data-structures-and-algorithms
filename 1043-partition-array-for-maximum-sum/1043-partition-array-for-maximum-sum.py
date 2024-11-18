class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n+1)

        for i in range(n):
            cur_sum, cur_max = 0, 0
            for j in range(i, max(-1, i-k), -1):
                cur_max = max(cur_max, arr[j])
                cur_sum = max(cur_sum, dp[j] + (i-j+1) * cur_max)
            dp[i+1] = cur_sum


        return dp[-1]
