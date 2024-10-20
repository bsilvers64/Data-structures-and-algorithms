class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1, t1 = collections.deque(), collections.deque()

        for i in s:
            if i != "#": s1.append(i)
            else:
                if s1: s1.pop()

        for i in t:
            if i != "#": t1.append(i)
            else:
                if t1: t1.pop()
        
        if len(s1) != len(t1): return False
        i = 0

        while i < len(s1):
            if s1[i] != t1[i]: return False
            i += 1

            
        return True