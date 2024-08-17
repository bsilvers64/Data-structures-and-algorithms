class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, ans, curr = 0, 0, 1
        N = len(nums)

        for r in range(N):
            curr *= nums[r]

            while (curr >= k) and l <= r:
                curr //= nums[l]
                l += 1

            ans += (r - l + 1)
            print(l, r)

        return ans