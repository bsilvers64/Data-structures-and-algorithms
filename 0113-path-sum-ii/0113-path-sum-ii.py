# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        nodes = []
        def dfs(root, pathSum):
            if not root: return None

            nodes.append(root.val)
            pathSum += root.val
            
            if not root.left and not root.right:
                if pathSum == targetSum:
                    paths.append(nodes[:])
            
            dfs(root.left, pathSum)
            dfs(root.right, pathSum)

            nodes.pop()
            pathSum -= root.val
             
        dfs(root, 0)
        return paths