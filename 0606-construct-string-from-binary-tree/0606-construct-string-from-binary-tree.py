# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = []
        def dfs(root):
            if root:
                ans.append(str(root.val))
                if root.left:
                    ans.append("(")
                    dfs(root.left)
                    ans.append(")")
                if not root.left and root.right:
                    ans.append("()")
                if root.right:
                    ans.append("(")
                    dfs(root.right)
                    ans.append(")")
        
        dfs(root)
        return "".join(ans)
