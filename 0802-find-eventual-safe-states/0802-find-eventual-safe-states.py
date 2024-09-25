class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        check = collections.defaultdict(bool)

        def dfs(node):
            if not node: return True
            res = True
            for neighbor in node:
                if neighbor in check:
                    if not check[neighbor]: return False
                    else: continue
                else:
                    check[neighbor] = False
                    res = res and dfs(graph[neighbor])
                    check[neighbor] = res
                    if not res: return res
            return res


        
        for i in range(len(graph)):
            if i not in check:
                check[i] = False
                check[i] = dfs(graph[i])

        return sorted([i for i in check if check[i]])

        