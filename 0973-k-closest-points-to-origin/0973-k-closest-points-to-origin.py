from heapq import heapify, heappop, heappush
from math import sqrt, pow
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        for i in points:
            heappush(dis, [-sqrt(pow(i[0], 2) + pow(i[1], 2)), i])
            if len(dis) > k:
                heappop(dis)

        return [i[1] for i in dis]