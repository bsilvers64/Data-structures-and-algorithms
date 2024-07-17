class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        if len(s) == 1: return s
        if len(s) == 2:
            if s[0] == s[1]: return s
            else: return s[0]
        
        i = 0

        while i < len(s):
            left, right = i-1, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(ans):
                    ans = s[left: right+1]
                left -= 1
                right += 1
            i += 1
        
        i = 0
        while i < len(s):
            left, right = i-1, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(ans):
                    ans = s[left: right+1]
                left -= 1
                right += 1
            i += 1
            
        return ans
