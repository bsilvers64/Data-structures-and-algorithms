class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        negative = 1
        if s == "": return 0
        if s[0] == '-': 
            negative = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        

        ans = 0
        for i in range(len(s)):
            if not s[i].isdigit():
                break
            else:
                ans = 10 * ans + int(s[i])
        
        ans *= negative

        ans = min(ans, 2 ** 31 - 1)
        ans = max(ans, -2 ** 31)
    
        return ans

