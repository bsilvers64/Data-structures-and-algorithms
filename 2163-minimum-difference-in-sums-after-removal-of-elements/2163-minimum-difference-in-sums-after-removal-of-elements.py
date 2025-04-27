from heapq import heappush, heappop
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)//3
        maxheap, minheap = [], []

        minsum = float('inf')

        tmp = [0] * (n*3)
        total = 0

        for i in range(len(nums)-1, n-1, -1):
            total += nums[i]
            heappush(minheap, nums[i])
            if len(minheap) > n: 
                total -= heappop(minheap)
            if len(minheap) == n: tmp[i] = total

        total = 0
        for i in range(len(nums)-n):
            total += nums[i]
            heappush(maxheap, -nums[i])
            if len(maxheap) > n:
                total -= -heappop(maxheap) 
            if len(maxheap) == n:
                minsum = min(minsum, total - tmp[i+1])

        return minsum
