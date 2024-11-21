class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)+1
        dp = [[0 for _ in range(amount+1)] for _ in range((n))]

        # because for 0 coins, we can make no amount
        for i in range(amount+1):
            dp[0][i] = 0

        # because for amount 0 we have 1 way no matter how many coins we have
        for i in range(n):
            dp[i][0] = 1
        
        for i in range(1, n):
            for j in range(1, amount+1):
                not_choose = dp[i-1][j]
                choose = 0 if (j-coins[i-1]) < 0 else dp[i][j-coins[i-1]]
                dp[i][j]  = not_choose + choose

        return dp[-1][-1]