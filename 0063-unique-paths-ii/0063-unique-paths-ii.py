class Solution:
    def uniquePathsWithObstacles(self, obs: List[List[int]]) -> int:
        if obs[0][0] == 1 or obs[-1][-1] == 1:
            return 0
        
        obs[0][0] = 1
        for i in range(1,len(obs)):
            obs[i][0] = 1 if obs[i][0] == 0 and obs[i-1][0] == 1 else 0
        
        for i in range(1,len(obs[0])):
            obs[0][i] = 1 if obs[0][i] == 0 and obs[0][i-1] == 1 else 0

        for i in range(1, len(obs)):
            for j in range(1, len(obs[0])):
                if not obs[i][j]: obs[i][j] = obs[i-1][j] + obs[i][j-1]
                else: obs[i][j] = 0 
        
        return obs[-1][-1]
        