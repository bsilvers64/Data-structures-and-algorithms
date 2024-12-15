# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(n1, n2):
            if n1 and n2:
                return n1.val == n2.val and dfs(n1.left, n2.right) and dfs(n1.right, n2.left)
            elif not n1 and not n2: return True
            else: return False

        return dfs(root.left, root.right)
        