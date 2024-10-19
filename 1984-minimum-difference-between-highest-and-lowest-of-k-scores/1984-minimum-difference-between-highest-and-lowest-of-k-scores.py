class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, -1
        while k:
            r += 1
            k -= 1
        ans = float('inf')
        while r < len(nums):
            ans = min(ans, nums[r]-nums[l])
            r += 1
            l += 1
        return ans

