import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x: x[0])

        memo = {}

        def backtrack(i):
            if i >= len(jobs): return 0
            if i in memo: return memo[i]

            # not including this interval
            res = backtrack(i+1)

            # including this interval and moving to the next non-overlapping interval
            j = bisect.bisect(jobs, (jobs[i][1], -1, -1))

            res = max(res, jobs[i][2] + backtrack(j))

            memo[i] = res
            return res
        
        return backtrack(0)