class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index, i = 1, 1

        while i < len(nums):
            if nums[i] != nums[i-1]:
                nums[index] = nums[i]
                index += 1
            i +=1 
        ans = index

        while index < len(nums):
            nums[index] = "_"
            index += 1

        return ans
