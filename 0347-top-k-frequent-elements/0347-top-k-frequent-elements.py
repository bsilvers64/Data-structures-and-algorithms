from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)

        for num in nums:
            frequency[num] += 1
        
        heap = []

        for num, count in frequency.items():
            heappush(heap, [count, num])
            if len(heap) > k:
                heappop(heap)
        
        result = []

        while heap:
            result.append(heappop(heap)[1])

        return result