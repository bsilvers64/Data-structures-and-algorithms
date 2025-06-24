class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        u, vi, vd = 0, 1, 2
        order = []

        graph = defaultdict(list)

        for c, p in pre:
            graph[c].append(p)

        state = [u] * n

        def dfs(c):
            if state[c] == vi: return False
            elif state[c] == vd: return True

            state[c] = vi

            for prereq in graph[c]:
                if not dfs(prereq): return False
            
            state[c] = vd
            order.append(c)
            return True
        
        for i in range(n):
            if state[i] == u: 
                if not dfs(i): return []

        return order