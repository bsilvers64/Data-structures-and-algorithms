class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        res = 0
        count = defaultdict(int)

        for num in nums:
            count[num] = max(count[num], count[k]) + 1
            res = max(res, count[num] - count[k])
        
        return res + count[k]