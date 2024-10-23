class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ans = 0
        mod = 10**9 + 7
        l, r = 0, len(nums) - 1
        nums.sort()

        for i, left in enumerate(nums):
            while (left + nums[r]) > target and i <= r:
                r -= 1
            if i <= r:
                ans += 2**(r-i)
                ans %= mod

        return ans
            