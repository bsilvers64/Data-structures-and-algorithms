class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        N = len(nums)
        k %= N
        reverse(0, N-1)
        reverse(0, k-1)
        reverse(k, N-1)
