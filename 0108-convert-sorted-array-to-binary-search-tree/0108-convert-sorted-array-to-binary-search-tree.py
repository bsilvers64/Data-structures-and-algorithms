# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def tree_make(l, r):
            if l > r: return None
            mid = (l + r)//2
            root = TreeNode(val=nums[mid])
            root.left = tree_make(l, mid-1)
            root.right = tree_make(mid+1, r)
            return root

        
        return tree_make(0, len(nums)-1)