class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf')] * (days[-1]+1)
        travel_days = set(days)
        dp[0] = 0

        for i in range(1, days[-1]+1):
            if i in travel_days:
                one_day_pass = costs[0] + dp[i-1]
                seven_day_pass = costs[1] + dp[i-7] if i-7 >= 0 else costs[1]
                thirty_day_pass = costs[2] + dp[i-30] if i-30 >= 0 else costs[2]
                dp[i] = min(one_day_pass, seven_day_pass, thirty_day_pass)
            else:
                dp[i] = dp[i-1]
        
        return dp[-1]