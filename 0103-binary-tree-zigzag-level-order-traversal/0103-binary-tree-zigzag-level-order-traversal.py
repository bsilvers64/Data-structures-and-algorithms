# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque()
        q.append(root)
        order = []
        flag = 1
        while q:
            number_of_nodes = len(q)
            level = []
            for i in range(number_of_nodes):
                if flag: 
                    root = q.pop()
                    if root.left:
                        q.appendleft(root.left)
                    if root.right:
                        q.appendleft(root.right)
                else:
                    root = q.popleft()
                    if root.right:
                        q.append(root.right)
                    if root.left:
                        q.append(root.left)
                level.append(root.val)

            order.append(level)
            flag = 0 if flag else 1
        
        return order