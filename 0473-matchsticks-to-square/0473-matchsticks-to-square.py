class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sides = [0] * 4
        length = sum(matchsticks) // 4
        if sum(matchsticks) / 4 != length: return False

        matchsticks.sort(reverse=True)

        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if matchsticks[i] + sides[j] <= length:
                    sides[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j] -= matchsticks[i]
            return False

        return backtrack(0)
