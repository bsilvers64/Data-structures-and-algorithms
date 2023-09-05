# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def haspathsum(self, root):
        if root:
            self.tsum += root.val
            ans = self.haspathsum(root.left) or self.haspathsum(root.right)
            if not root.left and not root.right and self.targetSum == self.tsum:
                return True
            self.tsum -= root.val
            return ans
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.tsum = 0
        self.targetSum = targetSum
        return self.haspathsum(root)

                
