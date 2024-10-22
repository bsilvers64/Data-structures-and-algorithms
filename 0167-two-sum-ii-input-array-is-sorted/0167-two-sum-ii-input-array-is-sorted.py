class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1

        while l <= r:
            total = nums[l] + nums[r]
            if total == target: return [l+1, r+1]
            elif total > target:
                total -= nums[r]
                r -= 1
            else:
                total -= nums[l]
                l += 1                
        