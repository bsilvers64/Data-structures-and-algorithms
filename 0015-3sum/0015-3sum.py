class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left = 0
        N = len(nums)
        ans = []

        nums.sort()

        while left < N:
            if left > 0 and nums[left-1] == nums[left]:
                left += 1
                continue
            if nums[left] > 0: break

            l, r = left + 1, N-1
            target = nums[left]
            while l < r:
                total = nums[left] + nums[l] + nums[r]
                if total == 0:
                    ans.append([nums[left], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: l += 1
                    while l < r and nums[r] == nums[r+1]: r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1

            left += 1
        
        return ans
                
            