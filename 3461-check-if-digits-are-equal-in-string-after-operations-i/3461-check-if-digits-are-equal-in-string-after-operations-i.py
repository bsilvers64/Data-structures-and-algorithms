class Solution:
    def hasSameDigits(self, s: str) -> bool:
        temp = []
        
        while len(s) != 2:
            for i in range(len(s)-1):
                temp.append(str((int(s[i]) + int(s[i+1])) % 10))
            s = "".join(temp)
            temp = []
        
        return s[0] == s[1]
