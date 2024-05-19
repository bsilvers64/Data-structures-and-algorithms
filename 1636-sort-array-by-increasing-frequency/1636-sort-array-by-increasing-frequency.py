class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        for k, v in count.items():
            bucket[v].append(k)
        ans = []
        print(bucket)
        for i in range(1, len(nums) + 1):
            for element in sorted(bucket[i], reverse=True):
                for _ in range(i):
                    ans.append(element)

        return ans