from heapq import heapify, heappush, heappop 
class Solution:
    def lastStoneWeight(self, stone: List[int]) -> int:
        stones = [i*-1 for i in stone]
        heapify(stones)

        while len(stones) > 1:
            x = heappop(stones) * -1
            y = heappop(stones) * -1
            if x != y:
                heappush(stones, abs(x - y)*-1)
            print(stones)
        
        if stones: return stones[0]*-1
        else: return 0 