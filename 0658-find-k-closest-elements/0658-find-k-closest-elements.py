import math
from io import StringIO
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        if len(arr) < k:
            return []
        
        heap = []
        
        for i in arr:
            if len(heap) < k:
                heappush(heap, (-1 * abs(i - x), i))
            else:
                if -1 * heap[0][0] > abs(i - x):
                    heappop(heap)
                    heappush(heap, (-1 * abs(i - x), i))
        
        return sorted([val for _, val in heap]) 