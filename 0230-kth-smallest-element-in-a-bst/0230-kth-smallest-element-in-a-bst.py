# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(root):
            nonlocal k
            if root:
                left = inorder(root.left)
                if left is not None: return left
                k -= 1
                if k == 0: return root.val
                right = inorder(root.right)
                if right is not None: return right
            else: return None
 
        
        return inorder(root)
