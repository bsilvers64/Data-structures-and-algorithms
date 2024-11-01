from collections import Counter
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        strmap = set()

        def overlap(s1, s2):
            c1, c2 = Counter(s1), Counter(s2)
            res = c1 + c2
            if max(res.values()) > 1:
                return True
            return False

        def backtrack(i):
            if i == len(arr):
                return len(strmap)
            res = 0
            if not overlap(arr[i], strmap):
                for c in arr[i]: strmap.add(c)
                res = backtrack(i+1)
                for c in arr[i]: strmap.remove(c)

            return max(res, backtrack(i+1))

        return backtrack(0) 
            
            
