# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque()
        queue.appendleft(root)
        level_order = []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop()
                level.append(node.val)
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
            level_order.append(level)
        return level_order