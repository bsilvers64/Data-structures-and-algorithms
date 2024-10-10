import math
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        adj = collections.defaultdict(list)
        for i, j in roads:
            adj[i].append(j)
            adj[j].append(i)
        
        def dfs(n, parent):
            nonlocal ans
            cnt = 1
            for nei in adj[n]:
                if nei != parent:
                    c = dfs(nei, n)
                    cnt += c
                    ans += math.ceil(c/seats)

            return cnt
        
        ans = 0
        dfs(0, -1)

        return ans
