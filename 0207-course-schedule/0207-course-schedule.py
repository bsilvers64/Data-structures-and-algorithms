class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        preq = collections.defaultdict(list)
        
        for i, j in pre:
            preq[i].append(j)
        visited = set()
        visiting = set()

        def dfs(node):
            if node in visited: return False
            elif node in visiting: return True
            
            visiting.add(node)
            for neighbor in preq[node]:
                if dfs(neighbor): return True
            visited.add(node)
            visiting.remove(node)
            return False

        for i in range(numCourses):
            if dfs(i): return False

        return True