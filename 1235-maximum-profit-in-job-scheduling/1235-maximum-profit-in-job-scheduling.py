class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        memo = {}
        def dfs(i):
            if i in memo: return memo[i]
            if i == len(intervals): return 0

            res = dfs(i+1)

            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            memo[i] = max(res, intervals[i][2] + dfs(j)) 
            return memo[i]
        
        return dfs(0)