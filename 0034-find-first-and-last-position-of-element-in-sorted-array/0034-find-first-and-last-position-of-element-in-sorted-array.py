class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        l, r = 0, N-1

        first, last = -1, -1

        # finding the left-most occurance of target
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                # target found, search even further left
                first = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1


        l, r = 0, N-1
        # finding the right-most occurance of target
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                # target found, search even further right
                last = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return [first, last]