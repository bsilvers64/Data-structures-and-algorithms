class Solution:
    def maxProfit(self, p: List[int]) -> int:
        max_p = 0
        lowest_dip = p[0]
        for i in p:
            lowest_dip = min(i, lowest_dip)
            max_p = max(max_p, i-lowest_dip)
        
        return max_p
