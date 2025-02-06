# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(root):
            if not root: return True
            if not root.left and not root.right: 
                return True if root.val == target else False

            left = dfs(root.left)
            if left: root.left = None
            right = dfs(root.right)
            if right: root.right = None

            if left and right and root.val==target: return True
            else: return False
        
        remove_root = dfs(root)
        return None if remove_root else root
        return root