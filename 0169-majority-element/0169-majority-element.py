import math
class Solution:
    def majorityElement(self, n: List[int]) -> int:
        res, count = n[0], 0

        for i in n:
            if count == 0:
                res = i
            if i == res:
                count+=1
            else:
                count-=1

        
        return res