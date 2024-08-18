class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        mp = collections.defaultdict(int)
        l, ans = 0, 0

        for r in range(len(nums)):
            mp[nums[r]] += 1
            while (mp[nums[r]] > k):
                mp[nums[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)
        
        return ans
            