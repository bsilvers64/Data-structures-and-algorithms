# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter = 0
    def helper(self, root):
        if not root:
            return 0
        max_depth_of_left = self.helper(root.left)
        max_depth_of_right = self.helper(root.right)
        self.diameter = max(max_depth_of_left + max_depth_of_right, self.diameter)
        return 1 + max(max_depth_of_left, max_depth_of_right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.diameter
        
        