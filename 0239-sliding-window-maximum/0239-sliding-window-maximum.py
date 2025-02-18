from heapq import heappush, heappop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        l, r = 0, 0

        res = []

        while r < len(nums):
            heappush(heap, [-nums[r], r])
            if (r-l+1) == k:
                while heap[0][1] < l: heappop(heap)
                res.append(-heap[0][0])
                l += 1
            r += 1

        return res