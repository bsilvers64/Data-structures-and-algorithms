# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0: return [target.val]
        graph = defaultdict(list)

        queue = deque()
        queue.appendleft(root)

        while queue:
            for _ in range(len(queue)):
                parent = queue.pop()
                if parent.left:
                    queue.append(parent.left)
                    graph[parent].append(parent.left)
                    graph[parent.left].append(parent)
                if parent.right:
                    queue.append(parent.right)
                    graph[parent].append(parent.right)
                    graph[parent.right].append(parent)
        


        visited = set()
        visited.add(target.val)
        queue.appendleft(target)
        result = []

        while queue:
            k -= 1
            result = []
            for _ in range(len(queue)):
                node = queue.pop()
                for neighbor in graph[node]:
                    if neighbor.val not in visited:
                        visited.add(neighbor.val)
                        queue.appendleft(neighbor)
                        result.append(neighbor.val)
            if k == 0:
                break
        
        return result




        
        return result