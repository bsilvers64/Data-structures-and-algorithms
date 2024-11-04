class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin, maxProfit = prices[0], 0
        for i in range(len(prices)):
            if currMin > prices[i]:
                currMin = prices[i]
            maxProfit = max(maxProfit, prices[i] - currMin)
        return maxProfit