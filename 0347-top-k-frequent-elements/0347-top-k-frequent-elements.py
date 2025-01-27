from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        N = len(nums)
        bucket = [[] for _ in range(N + 1)]


        for num, count in freq.items():
            bucket[count].append(num)

        i, res = N, []
        
        while len(res) != k:
            for num in bucket[i]: res.append(num)
            i -= 1
        
        return res
