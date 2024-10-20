class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index, i = 0, 0
        while i < len(nums):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
            i += 1
        while index < len(nums):
            nums[index] = 0
            index += 1