class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j, total = 0, 0, 0

        ans = 0
        N = len(nums)
        while (i < N):
            total += nums[i]
            while(nums[i] * (i - j + 1) > (total + k)):
                total -= nums[j]
                j += 1
            ans = max(ans, i - j + 1)
            i += 1
            print(i, j)
        return ans