# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(r1, r2):
            if r1 and r2:
                r1.val += r2.val
                if r1.left and r2.left: dfs(r1.left, r2.left)
                elif r2.left and not r1.left: r1.left = r2.left
                if r1.right and r2.right: dfs(r1.right, r2.right)
                elif r2.right and not r1.right: r1.right = r2.right
            
        if r1 and not r2: return r1
        elif r2 and not r1: return r2
        dfs(r1, r2)
        return r1