# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum = 0
    def helper(self, root, targetSum):
        if not root:
            return False
        self.sum += root.val
        print(self.sum, targetSum)
        ans = self.helper(root.left, targetSum) or self.helper(root.right, targetSum)
        if not (root.left or root.right) and self.sum == targetSum:
            print("hi")
            return True
        self.sum -= root.val
        return ans



    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.sum = 0
        if not root: return False
        return self.helper(root, targetSum)