class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def helper(i, j):
            if (i, j) in memo: return memo[(i, j)]
            if j == len(word2):
                if i >= len(word1): return 0
                else: return len(word1) - i
            else:
                if i == len(word1): return len(word2) - j


            if word1[i] == word2[j]:
                memo[(i, j)] = helper(i+1, j+1)
            else:
                insert = helper(i, j+1)
                delete = helper(i+1, j)
                replace = helper(i+1, j+1)
                memo[(i, j)] = 1 + min(insert, delete, replace)
            return memo[(i, j)]
        
        return helper(0, 0)