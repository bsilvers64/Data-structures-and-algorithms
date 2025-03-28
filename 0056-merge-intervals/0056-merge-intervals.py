class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        merged = []

        for i in range(len(intervals)):
            if not merged or intervals[i][0] > merged[-1][1]:
                merged.append(intervals[i])
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], intervals[i][1])]
                
        return merged
