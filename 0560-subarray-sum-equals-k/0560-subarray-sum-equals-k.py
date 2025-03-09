class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        res, prefix = 0, 0

        prefix_sum[0] = 1

        for num in nums:
            prefix += num

            if prefix - k in prefix_sum:
                res += prefix_sum[prefix-k]
            
            prefix_sum[prefix] += 1
            
        return res
