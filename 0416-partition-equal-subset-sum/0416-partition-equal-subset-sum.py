class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1: return False
        s //= 2
        mem = set()
        mem.add(0)
        mem.add(nums[0])

        for i in range(1, len(nums)):
            temp = set()
            for num in mem:
                temp.add(nums[i]+num)
                temp.add(num)
                if s in temp: return True
            mem = temp

        return False

