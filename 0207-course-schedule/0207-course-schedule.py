class Solution:
    def canFinish(self, numCourses: int, courses: List[List[int]]) -> bool:
        preq = collections.defaultdict(list)
        for a, b in courses:
            preq[a].append(b)
        
        visited = 2
        visiting = 1
        unvisited = 0
        state = [unvisited] * numCourses

        def dfs(node):
            if state[node] == visited: return True
            if state[node] == visiting: return False

            state[node] = visiting
            for i in preq[node]:
                if state[node] != visited and not dfs(i): return False
            
            state[node] = visited
            return True
            

        for i in range(numCourses):
            if not dfs(i): return False
        
        return True
