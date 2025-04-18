from heapq import heappush, heappop
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        N = len(weights)
        maxheap, minheap = [], []

        # maxheap will store the min k-1 splits and minheap will store the max k-1 splits

        for i in range(N-1):
            split = weights[i] + weights[i+1]
            heappush(minheap, split)
            heappush(maxheap, -split)

            # heap sizes will always remain k-1
            if len(maxheap) > (k-1): heappop(maxheap)
            if len(minheap) > (k-1): heappop(minheap)

        mincost, maxcost = 0, 0
        while maxheap: mincost += -heappop(maxheap)
        while minheap: maxcost += heappop(minheap)

        return maxcost - mincost