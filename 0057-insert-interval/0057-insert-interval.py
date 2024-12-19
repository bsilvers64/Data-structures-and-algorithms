class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        N = len(intervals)

        # append intervals till it don't overlap 
        i = 0
        while i < N and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        
        # merge intervals while they overlap
        while i < N and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        res.append(newInterval)

        # now merge the remaining non-overlapping intervals
        while i < N:
            res.append(intervals[i])
            i += 1
        
        return res