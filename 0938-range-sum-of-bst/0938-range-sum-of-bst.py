# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        def dfs(root):
            if root:
                nonlocal ans
                ans += root.val if (root.val <= high and root.val >= low) else 0
                if root.val >= low: dfs(root.left)
                if root.val <= high: dfs(root.right)
        
        dfs(root)
        return ans