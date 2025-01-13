class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}
        def robMax(i, loot):
            if i >= len(nums): return loot
            if (i, loot) in mem: return mem[(i, loot)]
            mem[(i, loot)] = max(robMax(i+2, loot+nums[i]), robMax(i+1, loot))
            return mem[(i, loot)]

        return robMax(0, 0)