import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[\W_]', '', s).lower()
        i = 0
        print(s)
        while i < len(s)//2:
            if s[i] != s[-1-i]:
                return False
            i+=1
        return True