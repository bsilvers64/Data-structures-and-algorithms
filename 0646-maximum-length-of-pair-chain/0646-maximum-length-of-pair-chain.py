class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        dp = [1] * len(pairs)
        pairs.sort(key = lambda x: x[1])
        ans = 1
        
        for i in range(1, len(pairs)):
            for j in range(0, i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
            ans = max(ans, dp[i])
        
        return ans