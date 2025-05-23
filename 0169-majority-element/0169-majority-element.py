class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxCount = 1
        majority_element = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == majority_element:
                maxCount += 1
            else:
                maxCount -= 1
                if maxCount <= 0:
                    majority_element = nums[i] 
                    maxCount = 1
        return majority_element