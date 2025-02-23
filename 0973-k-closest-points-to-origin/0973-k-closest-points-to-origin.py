from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            # pushing to max-heap - [distance from origin, coordinates]
            heappush(heap, [-(pow(x, 2) + pow(y, 2)), [x, y]])

            # if we have more than k coordinates in our max-heap, we will pop
            if len(heap) > k:
                heappop(heap)
        
        k_closest_points = []

        # extracting k closest points from origin from our max-heap
        while heap:
            _, coordinates = heappop(heap)
            k_closest_points.append(coordinates)
        
        return k_closest_points
