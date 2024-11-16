class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        N = len(scores)

        players = [[ages[i], scores[i]] for i in range(N)]
        dp = [0] * N
        players.sort(reverse=True)
        maxScore = 0

        for i in range(N):
            dp[i] = players[i][1]
            for j in range(i):
                if players[j][1] >= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
            maxScore = max(maxScore, dp[i])  
                   

        return maxScore