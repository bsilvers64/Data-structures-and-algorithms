class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        count = Counter(nums)

        def max_boost(b):
            curr, res = 0, 0
            for num in nums:
                if num == k: curr -= 1
                if num == b: curr += 1
                if curr < 0: curr = 0
                res = max(res, curr)
            return res

        res = 0
        for num in count: 
            res = max(res, max_boost(num))
        
        return count[k] + res

        