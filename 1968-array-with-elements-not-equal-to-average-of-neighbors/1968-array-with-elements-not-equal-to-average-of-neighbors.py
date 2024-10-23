class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        l, r = 0, len(nums)-1
        res = []
        while l <= r:
            res.append(nums[l])
            l += 1
            res.append(nums[r])
            r -= 1
        if len(nums) & 1: res.pop()
        return res