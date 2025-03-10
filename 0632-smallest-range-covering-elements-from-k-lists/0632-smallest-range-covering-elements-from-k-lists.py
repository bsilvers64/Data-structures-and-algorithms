from heapq import heappush, heappop
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        k = len(nums)
        left, right = nums[0][0], nums[0][0]
        min_heap = []

        for i in range(k):
            arr = nums[i]
            left = min(left, arr[0])
            right = max(right, arr[0])

            heappush(min_heap, (arr[0], i, 0)) # number, index of array, index of number in array
        
        res = [left, right]

        while True:
            num, i, idx = heappop(min_heap)
            idx += 1

            if idx == len(nums[i]): break

            heappush(min_heap, (nums[i][idx], i, idx))

            left = min_heap[0][0]
            right = max(right, nums[i][idx])

            if right - left < res[1] - res[0]:
                res = [left, right]


        return res