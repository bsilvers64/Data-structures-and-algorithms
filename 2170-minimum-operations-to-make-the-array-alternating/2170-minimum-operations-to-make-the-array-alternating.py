class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        odd, even = defaultdict(int), defaultdict(int)
        N = len(nums)

        for i in range(N):
            if i % 2 == 0:
                even[nums[i]] += 1
            else:
                odd[nums[i]] += 1
            
        odd_max, even_max = 0, 0
        odd_max_count, even_max_count = 0, 0

        for num, count in odd.items():
            if count > odd_max_count: 
                odd_max_count = count
                odd_max = num

        for num, count in even.items():
            if count > even_max_count: 
                even_max_count = count
                even_max = num


        odd_max_2, even_max_2 = 0, 0
        odd_max_2_count, even_max_2_count = 0, 0


        for num, count in odd.items():
            if count > odd_max_2_count and odd_max != num: 
                odd_max_2_count = count
                odd_max_2 = num

        for num, count in even.items():
            if count > even_max_2_count and even_max != num: 
                even_max_2_count = count
                even_max_2 = num
        
        if odd_max != even_max:
            return N - odd_max_count - even_max_count
        else:
            return min(
                N - odd_max_count - even_max_2_count,
                N - even_max_count - odd_max_2_count
            )