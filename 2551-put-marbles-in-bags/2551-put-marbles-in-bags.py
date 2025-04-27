from heapq import heappush, heappop
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        maxheap, minheap = [], []
        splits = []
        N = len(weights)
        maxsum = 0
        minsum = 0

        for i in range(N-1):
            splits.append(weights[i] + weights[i+1])

        for split in splits:
            heappush(minheap, split)
            heappush(maxheap, -split)
            if len(minheap) > k-1: heappop(minheap)
            if len(maxheap) > k-1: heappop(maxheap)

        while maxheap: minsum += (-heappop(maxheap))
        while minheap: maxsum += heappop(minheap)

        return maxsum - minsum

        
