from heapq import heappush, heappop
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for i in arr:
            if len(heap) < k:
                heappush(heap, [-abs(i-x), i])
            else:
                if heap[0][0] < -abs(i-x):
                    heappop(heap)
                    heappush(heap, [-abs(i-x), i])
                

        return sorted([num for dis, num in heap])
