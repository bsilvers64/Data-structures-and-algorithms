# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque()
        q.append(root)
        while q:
            curr = q.popleft()
            if curr :
                q.append(curr.left)
                q.append(curr.right)
            else:
                while q:
                    if q.popleft(): return False

        return True