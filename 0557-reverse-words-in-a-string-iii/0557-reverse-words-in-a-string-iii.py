class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)

        def rev(i, j):
            
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        
        l, r = 0, 0
        while r < len(s):
            if r == len(s)-1:
                rev(l, r)
            elif s[r] == " ":
                rev(l, r-1)
                l = r + 1
            r += 1
            
        return "".join(s)