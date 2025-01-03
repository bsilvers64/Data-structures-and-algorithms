# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root: return -1
            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)
            res = max(res, left+right)
            return max(left, right)
        
        dfs(root)
        return res