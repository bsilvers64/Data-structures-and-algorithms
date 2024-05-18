class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.defaultdict(int)
        for i in nums:
            count[i] += 1

        heap = []
        heapq.heapify(heap)

        for num, count in count.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [pair[1] for pair in heap]