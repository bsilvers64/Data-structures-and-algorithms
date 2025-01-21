class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
        
        VISITED = 2
        VISITING = 1
        UNVISITED = 0
        node_state = [UNVISITED] * numCourses

        def dfs(course):
            if node_state[course] == VISITED: return True
            elif node_state[course] == VISITING: return False
            
            node_state[course] = VISITING
            for pre in prereqs[course]:
                if not dfs(pre): return False

            node_state[course] = VISITED
            return True
        
        for course in range(numCourses):
            if not dfs(course): return False

        return True