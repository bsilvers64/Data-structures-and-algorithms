class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False

        target = total // 2
        sums = set()

        sums.add(0)
        sums.add(nums[0])

        for i in range(1, len(nums)):
            temp = sums.copy()
            for k in temp:
                s = nums[i] + k
                if s == target: return True
                sums.add(s)

        return False