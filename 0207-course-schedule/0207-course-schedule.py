class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        
        """ return if there exists a cycle in the graph starting 
            traversal from node """
        def dfs(node) -> bool:
            if node in visited: return False
            if node in visiting: return True

            visiting.add(node)

            for parent in graph[node]:
                if dfs(parent): return True

            visiting.remove(node)
            visited.add(node)

            return False

        
        visited = set()
        visiting = set()

        for course in range(numCourses):
            if course not in visited:
                if dfs(course): return False
        
        return True