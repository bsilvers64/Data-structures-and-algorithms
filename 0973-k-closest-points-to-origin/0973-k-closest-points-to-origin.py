import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for point in points:
            dis = pow(pow(point[0], 2) + pow(point[1], 2), 0.5)
            heapq.heappush(res, [-dis, point])
            if len(res) > k: heapq.heappop(res)
        
        ans = [i[1] for i in res]
        return ans