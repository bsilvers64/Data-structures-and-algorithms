class Solution:
    def longestPalindrome(self, s: str) -> str:
        r = 0
        max_len = 0
        result = s[0]

        while r < len(s):
            i, j = r-1, r+1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if (j-i+1) > max_len:
                    max_len = j-i+1
                    result = s[i:j+1]
                i -= 1
                j += 1
            
            i, j = r-1, r
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if (j-i+1) > max_len:
                    max_len = j-i+1
                    result = s[i:j+1]
                i -= 1
                j += 1

            r += 1

        return result