# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = []
        q.append([root, 1])
        ans = 1
        while q:
            temp = []
            for node, idx in q:
                if node.left: temp.append((node.left, idx*2))
                if node.right: temp.append((node.right, idx*2+1))

            if temp: ans = max(ans, temp[-1][1] - temp[0][1] + 1)
            q = temp
        
        return ans
