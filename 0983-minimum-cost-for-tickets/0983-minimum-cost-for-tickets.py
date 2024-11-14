class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}

        ans = float('inf')

        def dfs(i):
            if i in memo: return memo[i]
            if i == len(days):
                return 0

            memo[i] = float('inf')

            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i]+d: j+= 1
                memo[i] = min(memo[i], c + dfs(j))

            return memo[i]
        
        return dfs(0)

