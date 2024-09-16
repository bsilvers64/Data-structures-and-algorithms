# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q, ans = collections.deque(), []
        if not root: return []
        q.append(root)
        
        while q:
            N = len(q)
            temp = []
            while N:
                curr = q.popleft()
                temp.append(curr.val)
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
                N -= 1

            ans.append(temp)

        return ans