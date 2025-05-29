# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        numbers = []
        number = []

        def dfs(root):
            if not root: return None
            if not root.left and not root.right:
                number.append(str(root.val))
                numbers.append("".join(number))
                return True
            
            number.append(str(root.val))
            left = dfs(root.left)
            if left: number.pop()
            right = dfs(root.right)
            if right: number.pop()
            return True
        
        dfs(root)
        return sum([int(num) for num in numbers])

