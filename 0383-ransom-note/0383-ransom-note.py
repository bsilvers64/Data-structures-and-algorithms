class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charmap = [0] * 26
        for i in magazine: charmap[ord(i)-ord('a')] += 1
        for i in ransomNote: 
            charmap[ord(i)-ord('a')] -= 1
            if charmap[ord(i)-ord('a')] < 0: return False
        return True