class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def helper(i):
            # Base case: if we are at or past the last step, no more cost is needed
            if i >= len(cost):
                return 0
            
            # Check if result for this step is already calculated
            if i in memo:
                return memo[i]

            # Calculate the minimum cost for this step and store it in memo
            memo[i] = cost[i] + min(helper(i + 1), helper(i + 2))
            return memo[i]
        
        # Start from either step 0 or step 1 and choose the minimum path
        return min(helper(0), helper(1))
