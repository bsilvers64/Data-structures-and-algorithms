class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrays = 0

        prefix_sums = defaultdict(int)
        _sum = 0

        prefix_sums[0] = 1

        for num in nums:
            _sum += num
            if _sum-k in prefix_sums:
                subarrays += prefix_sums[_sum-k]
            prefix_sums[_sum] += 1
        
        return subarrays