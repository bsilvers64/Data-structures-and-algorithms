class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0: return [0]
        dp = [0] * (n+1)

        offset = 0

        for i in range(1, n+1):
            if not (i & (i-1)): offset = i
            dp[i] = 1 + dp[i-offset]
    
        return dp