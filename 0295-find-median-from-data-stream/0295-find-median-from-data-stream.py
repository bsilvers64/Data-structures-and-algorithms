from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        # large - min-heap and small - max-heap
        self.large = []
        self.small = []


    def addNum(self, num: int) -> None:
        # default push to max-heap
        heappush(self.small, -num)

        # make sure every num in max-heap (small) is smaller than every num in min-heap (larger)
        if (self.large and self.small and (self.small[0] * -1) > self.large[0]):
            val =  -1 * heappop(self.small)
            heappush(self.large, val)
        
        # make sure length of both heaps are about the same
        if len(self.large) > len(self.small) + 1:
            val = heappop(self.large)
            heappush(self.small, -val)
        
        if len(self.small) > len(self.large) + 1:
            val = -1 * heappop(self.small)
            heappush(self.large, val)
        

    def findMedian(self) -> float:
        if len(self.small) == len(self.large): return (-self.small[0] + self.large[0]) / 2
        elif len(self.small) > len(self.large): return -self.small[0]
        else: return self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()