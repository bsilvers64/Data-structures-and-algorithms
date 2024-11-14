class Solution:
    def mincostTickets(self, days: List[int], cost: List[int]) -> int:
        dp = [float('inf')] * (days[-1]+1)
        travel = set(days)
        dp[0] = 0

        for i in range(1, days[-1]+1):
            if i in travel:
                oneday = cost[0] + dp[i-1]
                sevenday = cost[1] + dp[i-7] if i - 7 >= 0 else cost[1]
                thtyday = cost[2] + dp[i-30] if i - 30 >= 0 else cost[2]
                dp[i] = min(oneday, sevenday, thtyday)
            else:
                dp[i] = dp[i-1]

        return dp[-1]