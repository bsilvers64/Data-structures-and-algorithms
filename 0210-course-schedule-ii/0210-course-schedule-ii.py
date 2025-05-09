class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        
        state = [0] * numCourses

        graph = defaultdict(list)

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        def dfs(node: int) -> bool:
            if state[node] == VISITED: return False
            if state[node] == VISITING: return True

            state[node] = VISITING

            for parent in graph[node]:
                if dfs(parent): return True
            
            state[node] = VISITED
            course_order.append(node)
            return False
                            
        course_order = []

        for course in range(numCourses):
            if state[course] == UNVISITED:
                if dfs(course): return []

        return course_order