# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(node):
            nonlocal res
            if not node: return 0
            leftChildSum = max(0, dfs(node.left)) 
            rightChildSum = max(0, dfs(node.right))
            res = max(res, node.val + leftChildSum + rightChildSum)
            return node.val + max(leftChildSum, rightChildSum)
        
        dfs(root)
        return res