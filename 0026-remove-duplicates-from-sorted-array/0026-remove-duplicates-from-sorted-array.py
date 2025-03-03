class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]: continue
            else:
                nums[index] = nums[i]
                index += 1
        result = index
        
        return result

