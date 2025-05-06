from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.small = []     # this is the max-heap
        self.large = []     # this is the min-heap
        

    def addNum(self, num: int) -> None:
        heappush(self.small, -num)

        # we make sure that every element of the min heap is smaller
        # than every element of the max heap

        if self.large and self.large[0] < (-self.small[0]):
            temp = -heappop(self.small)
            heappush(self.large, temp)
        
        # now we make sure that the heaps are of almost the same size +-1
        if len(self.small) > len(self.large) + 1:
            temp = -heappop(self.small)
            heappush(self.large, temp)
        elif len(self.large) > len(self.small) + 1:
            temp = heappop(self.large)
            heappush(self.small, -temp)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0])/2
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()