from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = Counter(nums)

        for num, count in freq.items():
            heappush(heap, (count, num))
            if len(heap) > k: heappop(heap)
        
        return [num for count, num in heap]
