import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []


        for i in arr:
            if len(heap) < k: 
                heapq.heappush(heap, [-abs(i-x), i])
            else:
                if -heap[0][0] < abs(i-x):
                    heapq.heappush(heap, [-abs(i-x), i])
                    heapq.heappop(heap)

        ans = []
        for i in heap:
            ans.append(i[1])
        
        return sorted(ans)