from collections import deque

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        d1, d2 = deque([]), deque([])

        for i in s:
            if i != '#':
                d1.append(i)
            else:
                if len(d1):
                    d1.pop()

        for i in t:
            if i != '#':
                d2.append(i)
            else:
                if len(d2):
                    d2.pop()

        print(d1, d2)
        if len(d1) != len(d2): return False

        for i, j in zip(d1, d2):
            if i != j:
                return False
        
        return True
        
            