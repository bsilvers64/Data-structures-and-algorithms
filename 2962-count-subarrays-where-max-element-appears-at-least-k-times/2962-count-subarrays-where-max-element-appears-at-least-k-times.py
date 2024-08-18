class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        nums_max = max(nums)
        N = len(nums)
        l, ans, curr = 0, 0, 0
        total_subarrays = N * (N + 1)//2 

        for r in range(N):
            if nums[r] == nums_max: curr += 1
            
            while curr >= k:
                if nums[l] == nums_max: 
                    curr -= 1
                l += 1

            ans += (r - l + 1)

        return total_subarrays - ans
