import math
class Solution:
    def majorityElement(self, n: List[int]) -> int:
        count = {}

        if len(n) < 3:
            return n[0]
        bar = math.floor(len(n)/2)
        for i in n:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
                if count[i] > bar:
                    return i

