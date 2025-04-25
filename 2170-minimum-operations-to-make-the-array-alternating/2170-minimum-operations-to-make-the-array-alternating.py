class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        odd_freq, even_freq = defaultdict(int), defaultdict(int)

        for i in range(len(nums)):
            if (i%2==0): even_freq[nums[i]] += 1
            else: odd_freq[nums[i]] += 1

        max_odd, max_odd_freq = 0, 0
        max_even, max_even_freq = 0, 0

        for num, count in odd_freq.items():
            if count > max_odd_freq:
                max_odd_freq = count
                max_odd = num

        for num, count in even_freq.items():
            if count > max_even_freq:
                max_even_freq = count
                max_even = num

        second_max_odd, second_max_odd_freq = 0, 0
        second_max_even, second_max_even_freq = 0, 0       

        for num, count in odd_freq.items():
            if count > second_max_odd_freq and num != max_odd:
                second_max_odd_freq = count
                second_max_odd = num

        for num, count in even_freq.items():
            if count > second_max_even_freq and num != max_even:
                second_max_even_freq = count
                second_max_even = num
        
        if max_odd != max_even: return len(nums) - max_odd_freq - max_even_freq
        else:
            return min(
                len(nums) - max_odd_freq - second_max_even_freq,
                len(nums) - max_even_freq - second_max_odd_freq
            )