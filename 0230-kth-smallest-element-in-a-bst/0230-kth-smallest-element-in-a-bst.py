# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        def dfs(node):
            nonlocal count
            if node:
                val = dfs(node.left)
                if val is not None: return val
                count += 1
                if k == count: return node.val
                return dfs(node.right)
            else:
                return None
        
        return dfs(root)

