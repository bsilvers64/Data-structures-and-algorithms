# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        queue = deque()
        graph = defaultdict(list)

        queue.appendleft(root)

        while queue:
            node = queue.pop()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                queue.appendleft(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                queue.appendleft(node.right)
        
        queue = deque()
        visited = set()
        k_away = []

        queue.append([target.val, 0])

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node, distance_to_node = queue.pop()
                if distance_to_node == k: k_away.append(node)
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.appendleft([neighbor, distance_to_node + 1])

                
        return k_away