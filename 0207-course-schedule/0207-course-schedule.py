class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        preq = collections.defaultdict(list)
        
        for i, j in pre:
            preq[j].append(i)
        visit = set()
        path = set()

        def dfs(node):
            visit.add(node)
            path.add(node)

            for n in preq[node]:
                if n not in visit:
                    if dfs(n): return True
                elif n in path: return True
            
            path.remove(node)
            return False



        for i in range(numCourses):
            if i not in visit:
                if dfs(i): return False
        
        return True
