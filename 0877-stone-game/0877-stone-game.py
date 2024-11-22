class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        # calc the max amount alice can get
        def dfs(l, r):
            if l > r: return 0
            if (l, r) in memo: return memo[(l, r)]

            # decide if its alice's chance. the diff will be odd if its alice chance else its bob's chance
            even = True if (r-l) % 2 else False
            left = piles[l] if even else 0
            right = piles[r] if even else 0
            
            memo[(l, r)] = max(piles[l] + dfs(l+1, r), piles[r] + dfs(l, r-1))
            return memo[(l, r)]
        
        return dfs(0, len(piles)-1) > (sum(piles))//2