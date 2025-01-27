class Solution:
    def longestPalindrome(self, s: str) -> str:
        i = 0
        max_len = 0
        max_len_string = ''
        while i < len(s):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > max_len:
                    max_len = r-l+1
                    max_len_string = s[l:r+1]
                l -= 1
                r += 1
                print(l, r)
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > max_len:
                    max_len = r-l+1
                    max_len_string = s[l:r+1]
                l -= 1
                r += 1
            
            i += 1

        return max_len_string
