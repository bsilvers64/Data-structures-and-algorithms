class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        M, N = len(nums1), len(nums2)
        memo = [[-1]*N for i in range(M)]

        def dfs(i, j):
            if i >= M or j >= N: return 0
            if memo[i][j] != -1: return memo[i][j]

            if nums1[i] == nums2[j]:
                memo[i][j] = 1 + dfs(i+1, j+1)
            else:
                memo[i][j] = max(dfs(i+1, j), dfs(i, j+1))

            return memo[i][j]

        return dfs(0, 0)