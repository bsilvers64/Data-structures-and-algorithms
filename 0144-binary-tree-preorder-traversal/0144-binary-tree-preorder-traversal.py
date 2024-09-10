# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        st = []

        while st or root:
            while root:
                ans.append(root.val)
                st.append(root.right)
                root = root.left
            root = st.pop()

        return ans