# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque()
        
        right_view = []

        if root: 
            queue.appendleft([root])
            right_view.append(root.val)
        else: return []


        while queue:
            level = queue.pop()
            new_level = []
            for node in level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            if new_level:
                right_view.append(new_level[-1].val)
                queue.appendleft(new_level)

        
        return right_view
