class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inc = {k:0 for k in range(1,n+1)}
        outg = {k:0 for k in range(1,n+1)}

        for i in trust:
            outg[i[0]] += 1
            inc[i[1]] += 1

        for k in range(1,n+1):
            if inc[k] == n-1 and not outg[k]: return k


        return -1