class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charmap = [0] * 26
        for i in s: charmap[ord(i)-ord('a')] += 1
        for i in t: charmap[ord(i)-ord('a')] -= 1
        for i in charmap: 
            if i != 0: return False
        return True
        
        