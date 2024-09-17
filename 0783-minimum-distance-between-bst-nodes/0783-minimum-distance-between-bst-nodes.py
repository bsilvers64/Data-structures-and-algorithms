# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev, curr = None, float('inf')
        
        def dfs(root):
            if root:
                nonlocal prev, curr
                dfs(root.left)
                if prev: curr = min(curr, abs(root.val-prev.val))
                prev = root
                dfs(root.right)

        
        dfs(root)
        return curr