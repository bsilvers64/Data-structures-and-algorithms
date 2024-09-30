class Solution:
    def findOrder(self, numCourses: int, courses: List[List[int]]) -> List[int]:
        preq = collections.defaultdict(list)
        for a, b in courses:
            preq[a].append(b)
        
        visited = 2
        visiting = 1
        unvisited = 0

        state = [unvisited] * numCourses

        ans = []

        def dfs(node):
            if state[node] == visited: return True
            if state[node] == visiting: return False

            state[node] = visiting

            for n in preq[node]:
                if state[n] != visited and not dfs(n): return False
            

            state[node] = visited

            ans.append(node)
            return True

        for i in range(numCourses):
            if state[i] == 0: 
                if not dfs(i): return []
        
        return ans
