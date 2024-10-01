class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preqs = collections.defaultdict(set)
        adj = collections.defaultdict(list)

        for pre, crs in prerequisites:
            adj[crs].append(pre)
        
        def dfs(crs):
            if crs not in preqs:
                preqs[crs] = set()
                for pre in adj[crs]:
                    preqs[crs] |= dfs(pre)
                preqs[crs].add(crs)
            return preqs[crs]
        
        res = []
        for i in range(numCourses):
            dfs(i)
        
        for u, v in queries:
            res.append(u in preqs[v])

        return res