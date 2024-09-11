# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(r1, r2):
            if not r1 and not r2:
                return True
            if r1 and r2:
                if r1.val != r2.val: return False
                return isSame(r1.left, r2.left) and isSame(r1.right, r2.right)
            else:
                return False
        
        def helper(r, sr):
            if not r: return False
            if isSame(r, sr): return True
            return helper(r.left, sr) or helper(r.right, sr)

        return helper(root, subRoot)