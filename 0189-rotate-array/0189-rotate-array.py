class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        def rev(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        l, r = 0, len(nums)-1
        rev(l, r)
        r = 0

        while r < k: r += 1

        rev(0, r-1)
        rev(r, len(nums)-1)


