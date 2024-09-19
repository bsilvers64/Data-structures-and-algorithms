# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {v:i for i,v in enumerate(inorder)}

        def helper(l, r, x):
            if l > r: return None
            print(x)
            root = TreeNode(preorder[x])
            index = idx[root.val]
            print(root.val, index)
            x = x+1 
            root.left = helper(l, index-1, x)
            if root.left: x = x+1
            root.right = helper(index+1, r, x)

            return root
        
        return helper(0, len(inorder)-1, 0)
