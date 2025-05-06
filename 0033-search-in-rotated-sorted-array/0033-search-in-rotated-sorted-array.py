class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first we find the minimum number
        l, r = 0, len(nums)-1

        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]: l = mid + 1
            else: r = mid
        
        if nums[l] <= target <= nums[-1]:
            r = len(nums)-1
        else:
            r = l - 1
            l = 0
        
        
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target: return mid
            elif nums[mid] > target: r = mid - 1
            else: l = mid + 1
        
        return -1
