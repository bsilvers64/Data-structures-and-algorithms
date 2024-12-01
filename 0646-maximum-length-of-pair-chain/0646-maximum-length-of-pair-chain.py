class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        ans = 0
        cur = float('-inf')
        
        for pair in pairs:
            if pair[0] > cur:
                ans += 1
                cur = pair[1]
        
        return ans