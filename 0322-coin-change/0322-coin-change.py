class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        coins.sort()
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                diff = i - coin
                if diff < 0: break
                dp[i] = min(dp[i], 1+dp[diff])

        return -1 if dp[-1] == float('inf') else dp[-1]
