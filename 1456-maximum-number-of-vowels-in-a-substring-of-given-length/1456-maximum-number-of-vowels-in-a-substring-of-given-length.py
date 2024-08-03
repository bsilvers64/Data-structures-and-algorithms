class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans, curr_vowel_count = 0, 0
        i, j = 0, 0

        N = len(s)
        vowel = {'a', 'e', 'i', 'o', 'u'}

        while (i < N):
            if s[i] in vowel: curr_vowel_count += 1
            if (i - j + 1 == k):
                ans = max(ans, curr_vowel_count)
                if s[j] in vowel: curr_vowel_count -= 1
                j += 1
                
            i += 1
        return ans