class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans, N = [], len(nums)

        l = 0
        while l < N:
            if l > 0 and nums[l] == nums[l-1]: 
                l += 1
                continue
            if nums[l] > 0: break
            
            r = N - 1
            low = l + 1
            while low < r:
                total = nums[l] + nums[low] + nums[r]
                if total == 0: 
                    ans.append([nums[l], nums[low], nums[r]])
                    low += 1
                    r -= 1
                    while low < r and nums[low] == nums[low-1]: low += 1
                    while low < r and nums[r] == nums[r+1]: r -= 1
                elif total > 0:
                    r -= 1
                else:
                    low += 1
            l += 1

        return ans
            
