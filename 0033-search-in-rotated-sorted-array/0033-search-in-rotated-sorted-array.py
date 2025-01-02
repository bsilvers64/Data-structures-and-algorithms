class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)-1
        l, r = 0, n
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]: l = mid+1
            else: r = mid
        min_index = l

        #if min_index == 0: l, r = 0, n
        if nums[min_index] <= target <= nums[n]:
            l, r = min_index, n 
        else:
            l, r = 0, min_index - 1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target: return mid
            elif nums[mid] < target: l = mid + 1
            else: r = mid - 1 

        return -1           