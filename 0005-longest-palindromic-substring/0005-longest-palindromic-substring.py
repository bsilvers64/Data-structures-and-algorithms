class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 1
        index = [0, 0]

        for i in range(len(s)):
            l, r = i-1, i+1

            while l > -1 and r < len(s) and s[l] == s[r]:
                if res < r-l+1:
                    res = r-l+1
                    index = [l, r]
                l -= 1
                r += 1
            
            l, r = i-1, i
            while l > -1 and r < len(s) and s[l] == s[r]:
                if res < r-l+1:
                    res = r-l+1
                    index = [l, r]
                l -= 1
                r += 1

        return s[index[0]: index[1]+1]