class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i < coin: break
                dp[i] = min(dp[i], 1 + dp[i-coin])

        return dp[-1] if dp[-1] != float('inf') else -1