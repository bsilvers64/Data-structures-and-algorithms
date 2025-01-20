class Solution:
    def pacificAtlantic(self, height: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        M, N = len(height), len(height[0])

        def dfs(i, j, prev_height, ocean):
            if 0 <= i < M and 0 <= j < N and (i, j) not in ocean and height[i][j] >= prev_height:
                ocean.add((i, j))
                dfs(i, j+1, height[i][j], ocean)
                dfs(i+1, j, height[i][j], ocean)
                dfs(i, j-1, height[i][j], ocean)
                dfs(i-1, j, height[i][j], ocean)
        
        # in the atlantic ocean -
        for i in range(M):
            if (i, N-1) not in atlantic:
                dfs(i, N-1, -1, atlantic)
        for j in range(N):
            if (M-1, j) not in atlantic:
                dfs(M-1, j, -1, atlantic)        

        # in the pacific ocean -
        for i in range(M):
            if (i, 0) not in pacific:
                dfs(i, 0, -1, pacific)
        for j in range(N):
            if (0, j) not in pacific:
                dfs(0, j, -1, pacific)
        
        ans = []
        for i in range(M):
            for j in range(N):
                if (i, j) in pacific and (i, j) in atlantic:
                    ans.append([i, j])  

        return ans