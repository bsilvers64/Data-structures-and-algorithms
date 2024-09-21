class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mp = {k:[[], 0] for k in range(1,n+1)}

        for i in trust:
            mp[i[0]][0].append(i[1])
            mp[i[1]][1] += 1

        for key in mp:
            if mp[key][1] == n-1 and not mp[key][0]: return key


        return -1