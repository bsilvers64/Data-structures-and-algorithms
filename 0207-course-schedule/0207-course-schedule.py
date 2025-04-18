class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, preq in prerequisites:
            graph[course].append(preq)
        
        visited = set()
        visiting = set()

        def dfs(node):
            if node in visited:
                return False
            if node in visiting:
                return True
            
            visiting.add(node)
            for prereq in graph[node]:
                if dfs(prereq): return True
            
            visiting.remove(node)
            visited.add(node)
            return False
        
        for course in range(numCourses):
            if course not in visited and dfs(course): return False
        
        return True