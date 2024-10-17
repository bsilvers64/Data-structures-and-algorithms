import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visit = set()
        minheap = [[0, points[0][0], points[0][1]]]

        ans = 0
        while minheap:
            dis, u, v = heapq.heappop(minheap)
            if (u, v) in visit: continue
            visit.add((u, v))

            ans += dis
            for i, j in points:
                if (i, j) not in visit:
                    w = abs(i - u) + abs(j - v)
                    heapq.heappush(minheap, [w, i, j])
 
        return ans