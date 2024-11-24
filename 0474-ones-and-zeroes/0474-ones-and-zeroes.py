class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}
        N = len(strs)

        def helper(i, m, n):
            if i >= N: return 0
            if (i, m, n) in memo: return memo[(i, m, n)]

            nZeroes = strs[i].count("0")
            nOnes = strs[i].count("1")
            
            if nZeroes > m or nOnes > n: 
                 memo[(i, m, n)] = helper(i+1, m, n)
            else:
                include =  1 + helper(i+1, m - nZeroes, n - nOnes)
                exclude = helper(i+1, m, n)

                memo[(i, m, n)] = max(include, exclude)
            return memo[(i, m, n)]

        return helper(0, m, n)



