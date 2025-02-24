class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # keeps track of all nodes which we have visited
        visited = set()

        # keeps track of nodes we are visiting currently / or are in our current path
        visiting = set()

        # create adjacency list of courses -> their pre-requisites
        graph = defaultdict(list)

        for course, pre_req in prerequisites:
            graph[course].append(pre_req)

        # depth-fist-search to explore the graph
        def dfs(node):
            # node is already visited so no need to explore
            if node in visited:
                return False

            # we came across this node again, so cycle detected
            if node in visiting:
                return True
            
            # we are now visiting this node
            visiting.add(node)

            # explore the node's neighbors
            for neighbor in graph[node]:

                # if function returns true means cycle exists
                if dfs(neighbor): return True
            

            # finished visiting and the node is now visited
            visiting.remove(node)
            visited.add(node)

            courses_order.append(node)

            # no cycle was found so far so return False
            return False
        

        courses_order = []

        for course in range(numCourses):

            # if cycle exists, means we cannot finish all courses
            if dfs(course): return []
        
        return courses_order

