# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root: return []
        q = collections.deque()
        q.append(root)
        flag = 0
        while q:
            N = len(q)
            temp = []
            while N:
                curr = q.popleft()
                temp.append(curr.val)
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
                N -= 1
            if flag: temp = temp[::-1]
            flag = 0 if flag else 1
            ans.append(temp)
        return ans