class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        
        for num in nums:
            counter[num] += 1
        
        result = []

        bucket = [None] * (len(nums)+1)

        for num, count in counter.items():
            if not bucket[count]:
                bucket[count] = []
            bucket[count].append(num)

        for i in range(len(bucket)-1, -1, -1):
            if bucket[i]: 
                for num in bucket[i]:
                    result.append(num)
                    if len(result) == k:
                        return result

    