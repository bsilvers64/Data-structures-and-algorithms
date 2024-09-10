# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root: return [True, 0]
            left = helper(root.left)
            right = helper(root.right)
            is_balanced = True
            if not left[0] or not right[0] or abs(left[1] - right[1]) > 1: is_balanced = False
            return [is_balanced, 1 + max(left[1], right[1])]

        if helper(root)[0] == False: return False
        return True